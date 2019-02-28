import requests
import mysql.connector

# The below is for connecting to mySQL, use your login and password and the database name
# see the declaration below, replace the values inside the angled brackets
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="!Ramani@72",
    database="simplymac",
)
my_cursor = my_db.cursor(buffered=True)


headers = {
    'Authorization': "Basic ZGF0YS5hcGkuYWNjZXNzQHNpbXBseW1hYzpkY2NQR3pEdDR2ekhyY3U=",
    'cache-control': "no-cache",
}

payload = ""
querystring = {"IncludeDisabled": ""}
url = "https://dataconnect.iqmetrix.net/lists/categorynumber"
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
# parent_id = 0
# item_parent_id = 0
# id = 0

response_output = response.json()

# region Function to insert nulls into all the Level columns depending on category path
# The below function will insert null values starting from the columns where there is no
# category path


def insert_null_in_level_columns(level_no, total_no_levels):
    col_none_tuple = ()
    for level in range(level_no, total_no_levels):
        col_none_tuple += (None,)
    return col_none_tuple

# endregion

# Below function to insert data into each column of category table.
# The function is a tricky one because for every row in the table Level1 and Level2 will always have values
# Level2 will be null when you are looking at the first entry like 'Inventory Tree'
# The function uses CategoryPath to find what values to be inserted into Level3 to Level8 and the total number of
# values are not hardcoded with a variable which can be changed and everything should work. There are other small tweaks
# that are applied like when splitting the category path it is splitting with a first element as blank which we
# do not need, so we kind of take it out from the list and create a new one with the rest of the elements.

# region Function Insert Level details to the query


def insert_levels_to_query(id, parent_id, description, level1, level2, total_level, no_of_level, cat_path):
    category_path = cat_path.split(' >> ')[1:len(cat_path)]
    col_tuple = (id, parent_id, description, level1, level2,)
    if len(category_path) > 0:
        for cat_len in range(len(category_path)):
            col_tuple += (category_path[cat_len],)
        col_tuple += insert_null_in_level_columns(no_of_level+1, total_level+1)
    else:
        col_tuple += insert_null_in_level_columns(3, total_level + 1)
    return col_tuple

# endregion


# region Create Table category SQL Script

# CREATE TABLE category (
# 	ID bigint NOT NULL,
#     ParentID bigint NULL,
#     Description varchar(1000) NOT NULL,
#     Level1 varchar(1000) NOT NULL,
#     Level2 varchar(1000) NULL,
#     Level3 varchar(1000) NULL,
#     Level4 varchar(1000) NULL,
#     Level5 varchar(1000) NULL,
#     Level6 varchar(1000) NULL,
#     Level7 varchar(1000) NULL,
#     Level8 varchar(1000) NULL,
#     PRIMARY KEY (ID)
#
# )

# endregion

# The column list only contains 4 values as there are is logic involved in finding the rest
# of the columns like Level3, Level4, Level5, Level6, Level7, Level8
# for now there are only 8 levels in future if they grow then you need to change the Insert query down below to add
# that extra column(s) and also the values too. The rest of the logic should fall in place.

column_list = ['ID', 'ParentID', 'Description', 'Level']

# The query now contains only 8 levels for now

sql_insert_query = 'Insert into category (ID, ParentID, Description, Level1, Level2, Level3, Level4, Level5, Level6,' \
                   'Level7, Level8) values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
row_data = []
# This value needs to change if the the count of Level columns in the database changes from 8 to something
total_level_columns = 8

# The below loop will go through the Json output, and as the output is starting with main id which 10, that's the
# parent to all IDs, if the json is not returning this as the first element in the output this logic won't work.
# we kind of need to change it accordingly then, either by hard coding the first rows and the 2nd row by that what
# I mean is the first row in the SQL table and the 2nd row in the SQL table should look like this
# As you can see what I am talking about
# [ID, Parent ID, Description,    Level1,       , Level2,   Level3, Level4, Level5 Level6, Level7, Level8]
# [10,  Null,     Inventory Tree, Inventory Tree,  Null,     Null,   Null,   Null,   Null,  Null,   Null]
# [1010, 10,     Products,        Inventory Tree,  Products, Null,   Null,   Null,   Null,  Null,   Null]

for item in response_output:
    category_tuple = ()
    len_of_id = len(str(item['ID']))/2
    for column in column_list:
        if len_of_id == 1:
            Level_1 = item['Description']
            Level_2 = None
        if len_of_id == 2:
            Level_2 = item['Description']
        if column == 'Level':
            category_tuple = insert_levels_to_query(item['ID'], item['ParentID'], item['Description'], Level_1,
                                                    Level_2, total_level_columns, int(len_of_id), item['CategoryPath'])
    row_data.append(category_tuple)

my_cursor.executemany(sql_insert_query, row_data)
my_db.commit()
