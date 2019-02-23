import requests
import json
import mysql.connector

url = "https://acuityscheduling.com/api/v1/appointments"

# querystring = {"minDate": "02/01/2019", "maxDate": "02/08/2019"}

payload = ""
headers = {
    'Authorization': "Basic MTcwNDI5NjM6ZTEyYzQ3YWJlMDNjMDI0OGY0MzllNjgyZWQyMjgzMzAg",
    'cache-control': "no-cache",
    'content-type' : 'application/json'
    }

response = requests.request("GET", url, data=payload, headers=headers)

decoded_response = response.text.encode("UTF-8")

# json_data = json.loads(response.text)
# jsonResponse  = json.loads(decoded_response)
print(len(response.json()))
noofrows = len(response.json())
err_flag = False


# colnames
ID = 'id'  # int
FirstName = 'firstName'  # str
LastName = 'lastName'  # str
Phone = 'phone'  # str
Email = 'email'  # str
Date = 'date'  # str
time = 'time'  # str
EndTime = 'endTime'  # str
DateCreated = 'dateCreated'  # str
DateTimeCreated = 'datetimeCreated'  # str
DateTime = 'datetime'  # str
Price = 'price'  # str
PriceSold = 'preceSold'  # str
Paid = 'paid'  # str
AmountPaid = 'amountPaid'  # str
Type = 'type'  # str
AppointmentTypeID = 'appointmentTypeID'  # int
Category = 'catetory'  # str
Duration = 'duration'  # str
Calendar = 'calendar'  # str
CalendarId = 'calendarID'  # int
Certificate = 'certificate'  # str
ConfirmationPage = 'confirmationPage'  # str
Location = 'location'  # str
Notes = 'notes'  # str
TimeZone = 'timezone'  # str
CalendarTimeZone = 'calendarTimezone'  # str
Cancelled = 'canceled'  # bool
CanClientCancel = 'canClientCancel'  # bool
CanClientReschedule = 'canClientReschedule'  # bool
Labels = 'labels'  # NoneType

columnList = ['ID', 'FirstName', 'LastName', 'Phone', 'Email', 'Date', 'Canceled', 'CanClientCancel']

columnsDict = {'ID': ID, 'FirstName':  FirstName, 'LastName': LastName, 'Phone': Phone, 'Email': Email, 'Date': Date,
               'Cancelled': Cancelled, 'CanClientCancel': CanClientCancel}

def creatingInsertSQLQuery():
    mysql.connector.

def creatingSQLQuery(jsonoutput):


    row = 0
    sqlquerycols = 'Insert into Table1 ('
     # 'Insert into Table1 ('
    noOfCol = 0
    for key, value in columnsDict.items():
        if noOfCol < len(columnsDict) - 1:
            sqlquerycols += key + ', '
        else:
            sqlquerycols += key + ') values ('
        noOfCol += 1
    print(sqlquerycols)
    sqlQuery = ''
    noOfCol = 0
    for item in jsonoutput:
        sqlQuery += "\n" + sqlquerycols
        for key, value in columnsDict.items():

            print(item['canceled'])
            if noOfCol < len(columnsDict) - 1:
                if type(item[value]) is str:
                    sqlQuery += "'" + item[value] + "',"
                elif type(item[value]) is int:
                    sqlQuery += str(item[value]) + ","
                elif type(item[value]) is bool:
                        sqlQuery += str(item[value]) + ","
            else:
                if type(item[value]) is str:
                    sqlQuery += "'" + item[value] + "' )"
                elif type(item[value]) is int:
                    sqlQuery += str(item[value]) + ')'
                elif type(item[value]) is bool:
                        sqlQuery += str(item[value]) + " ) "
            noOfCol += 1
            print(sqlQuery)
    print(sqlQuery)





def loopingJsonObject(jsonoutput):
    row = 0
    sqlQuery = 'Insert into Table1 ('
    # + ID + ',' + FirstName + ',' + LastName + ',' + Phone + ',' + Email + ') Values'


    for item in jsonoutput:
        sqlQuery += item[ID]
        row += 1
        print("\nThis is row " + str(row) + "\n")
        print(len(item))
        noOfCol = 0
        for item1 in item:

            # print(item1 + ": " + str(item[item1]) + " is a " + str(type(item[item1])))
            if noOfCol < len(item) -1:
                sqlQuery += item1 + ', '
            else:
                sqlQuery += item1
            noOfCol += 1
    sqlQuery += ') Values ( '
    print(sqlQuery)
    for item in jsonoutput:
        row += 1
        print("\nThis is row " + str(row) + "\n")
        for item1 in item:
            # print(item1 + ": " + str(item[item1]) + " is a " + str(type(item[item1])))
            sqlQuery += str(item[item1])

    sqlQuery += ' )'
    print(sqlQuery)
# creatingSQLQuery(response.json())
printKeys()

# for item in response.json():
#    print(item)




