import numpy as np
import requests

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

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# print(response.json())

url = "https://dataconnect.iqmetrix.net/inventory/ProductMasterList"

querystring = {"LanguageCode": "", "StoreIDLoggedIn": "1", "ProductType": "0",
               "SearchMethod": "0", "SearchCriteria": "10", "Enabled": "2", "CompanyID": ""}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "299c9d03-b032-4319-8090-7942a1756200"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(len(response.json()))

for item in response.json():
    print(item)
