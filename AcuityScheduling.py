import requests

url = "https://acuityscheduling.com/api/v1/appointments"

payload = ""
headers = {
    'Authorization': "Basic MTcwNDI5NjM6ZTEyYzQ3YWJlMDNjMDI0OGY0MzllNjgyZWQyMjgzMzA=",
    'cache-control': "no-cache",
    'Postman-Token': "95d7e05b-22f2-4ecd-b967-17251b5c3633"

    }
#
response1 = requests.request("GET", url, data=payload, headers=headers)

colNames = 






