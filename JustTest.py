import numpy as np
import requests
import mysql.connector
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="!Ramani@72",
    database="simplymac",
)
my_cursor = my_db.cursor(buffered=True)


columnList = ['id', 'firstName', 'lastName', 'phone', 'email', 'date', 'canceled', 'canClientCancel']

# sql_query = 'Insert into appointmentScheduling1 (' + map(lambda(y): x in y, columnList) + ')'

x = 'Test'

m1 = np.array([[5, 12, 6],[-3, 0, 14]])

m2 = np.array([[9, 8, 7], [1, 3, -5]])

t = np.array([m1, m2])
print(t)
# print(m1)

x = np.array([2, 8, -4])
y = np.array([1, -7, 3])
print(np.dot(x, y))

columnList = ['id', 'firstName', 'lastName', 'phone', 'email', 'date', 'canceled', 'canClientCancel']


url = "https://dataconnect.iqmetrix.net/reports/inventorylistingreport"

querystring = {"LanguageCode": "", "LocationTypeIDs": "19", "LocationType": "Store", "BinStatus": "10", "QtyStatus": "4"
               , "BlindInventory": "", "CategoryNumber": ""}

payload = ""
headers = {
    'Authorization': "Basic ZGF0YS5hcGkuYWNjZXNzQHNpbXBseW1hYzpkY2NQR3pEdDR2ekhyY3U=",
    'cache-control': "no-cache",
    'Postman-Token': "95c57c62-807f-4839-811b-30dcda2aea11"
    }

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# print(response.json())

url = "https://dataconnect.iqmetrix.net/inventory/ProductMasterList"

querystring = {"LanguageCode": "", "StoreIDLoggedIn": "1", "ProductType": "0",
               "SearchMethod": "0", "SearchCriteria": "10", "Enabled": "2", "CompanyID": ""}

payload = ""
headers = {
    'Authorization': "Basic ZGF0YS5hcGkuYWNjZXNzQHNpbXBseW1hYzpkY2NQR3pEdDR2ekhyY3U=",
    'cache-control': "no-cache",
}

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring,)

# print(len(response.json()))

# for item in response.json():
#     print(item)


test = abs(len(str(10101713)) / 2)

print(test)


# querystring = {"IncludeDisabled":""}
# url = "https://dataconnect.iqmetrix.net/lists/categorynumber"
# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
# parent_id = 0
# item_parent_id = 0
# id = 0
# for item in response.json():
#     print('Parent ID is {}'.format(item['ParentID']))
#     id = max(id, int(item['ID']))
#     if item['ParentID'] is not None:
#         item_parent_id = max(item_parent_id, int(item['ParentID']))
# print('The max level so far is {}, parent id is {} and  id is {}'.format(str(int(abs(len(str(item_parent_id))/2))),
#                                                                          item_parent_id, id))

sz  = ""

sz = sz.split(' >> ')[1:len(sz)]
print ('Len of sz is {}'.format(len(sz)))

str1 = " >> Hero Products (iCU's) >> Pre-Owned CPU's and iOS >> Pre-Owned iPhones >> CPO iPhone 7".split(' >> ')
print('The total no of elements in str are {}'.format(len(str1)))

for str2 in str1:
    print(str2)
for level in range(0, len(str1)):
    print(str1[level])
print('str 0 is {}', str1[0])
print('str 1 is {}', str1[1])
print('str 2 is {}', str1[2])
print('str 3 is {}', str1[3])
print('str 4 is {}', str1[4])


print(type(str1))
str1 = str1[1:len(str1)]
# print(str3)
print('str 0 is {}', str1[0])
print('str 1 is {}', str1[1])
print('str 2 is {}', str1[2])
print('str 3 is {}', str1[3])
print('str 4 is {}', str1[4])
st_tuple = ()
row_data = []
st_tuple = (1, None, 'Inventory', 'Inventory', None, None, None, None, None, None, None)
row_data.append(st_tuple)
st_tuple = (2, None, 'Inventory', 'Inventory', None, None, None, None, None, None, None)
row_data.append(st_tuple)
st_tuple = (3, None, 'Inventory', 'Inventory', None, None, None, None, None, None, None)
row_data.append(st_tuple)
st_tuple = (4, None, 'Inventory', 'Inventory', None, None, None, None, None, None, None)
row_data.append(st_tuple)


# st_tuple += (1, "NULL", 'Inventory', 'Inventory', "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL")
# row_data.append(st_tuple)
# st_tuple += (2, "NULL", 'Inventory', 'Inventory', "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL")
# row_data.append(st_tuple)
# st_tuple += (3, "NULL", 'Inventory', 'Inventory', "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL")
# row_data.append(st_tuple)
# st_tuple += (4, "NULL", 'Inventory', 'Inventory', "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL")
# row_data.append(st_tuple)



# st_tuple += (None,)

# sql_insert_query = 'Insert into category (ID, ParentID, Description, Level1, Level2, Level3, Level4, Level5, Level6,' \
#                    'Level7, Level8) values( 1, NULL, \'Inventory\',\'Inventory\', Null, NUll, Null, NUll, Null, ' \
#                    'Null, Null)'
print(row_data)
#
#
sql_insert_query = 'Insert into category (ID, ParentID, Description, Level1, Level2, Level3, Level4, Level5, Level6,' \
                    'Level7, Level8) values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

print(sql_insert_query)
# my_cursor.executemany(sql_insert_query,row_data)
# my_cursor.executemany(sql_insert_query, row_data)
# my_db.commit()

