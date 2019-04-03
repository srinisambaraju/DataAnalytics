import requests
import mysql.connector
import json

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

response_output = requests.get('https://dataconnect.iqmetrix.net/inventory/ProductMasterList?LanguageCode='
                               '&StoreIDLoggedIn=1&ProductType=0&SearchMethod=0&SearchCriteria=10&CompanyID=14205'
                               '&Enabled=2', data=payload, headers=headers)

# with open('c:\\srini\\productmaster.json') as f:
#     data = json.load(f)
# json_output = json.load('c:\\srini\\productmaster.json')
row_count = 0
print('The no of rows fetched from product master are {}'.format(len(response_output.json())))
for item in response_output:
    print(item)
    row_count += 1
    if 100 < row_count:
        break

