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

with open('c:\\srini\\productmaster.json') as f:
    data = json.load(f)
# json_output = json.load('c:\\srini\\productmaster.json')

for item in data:
    print(item)
    break

