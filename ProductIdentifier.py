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

url = "https://dataconnect.iqmetrix.net/lists/productidentifier"

querystring = {"IncludeDisabled": "", "CategoryNumbers": "", "SearchTerm": ""}
payload = ""

headers = {
    'Authorization': "Basic ZGF0YS5hcGkuYWNjZXNzQHNpbXBseW1hYzpkY2NQR3pEdDR2ekhyY3U=",
    'cache-control': "no-cache",
}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

column_list = ['ID', 'Description', 'CategoryNumber', 'ProductEnabled', 'SpecialProductID', 'GlobalProductID']

sql_insert_query = 'Insert into productidentifier (ID, Description, CategoryNumber, ProductEnabled, ' \
                   'SpecialProductID, GlobalProductID) values (%s, %s, %s, %s, %s, %s)'
row_data = []
for item in response.json():
    col_tuple = ()
    for column in column_list:
        col_tuple += (item[column],)

    row_data.append(col_tuple)

my_cursor.executemany(sql_insert_query, row_data)
my_db.commit()
