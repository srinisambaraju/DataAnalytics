import requests
import mysql.connector

# The below is for connecting to mySQL, use your login and password and the database name
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="!Ramani@72",
    database="acuityscheduling"
)

print(my_db)
my_cursor = my_db.cursor()
url = "https://acuityscheduling.com/api/v1/appointments"
querystring = {"minDate": "02/01/2019", "maxDate": "02/02/2019"}
payload = ""
headers = {
    'Authorization': "Basic MTcwNDI5NjM6ZTEyYzQ3YWJlMDNjMDI0OGY0MzllNjgyZWQyMjgzMzA=",
    'cache-control': "no-cache",
    'Postman-Token': "95d7e05b-22f2-4ecd-b967-17251b5c3633"

    }
#
response1 = requests.request("GET", url, data=payload, headers=headers, params=querystring)


# col names
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
PriceSold = 'priceSold'  # str
Paid = 'paid'  # str
AmountPaid = 'amountPaid'  # str
Type = 'type'  # str
AppointmentTypeID = 'appointmentTypeID'  # int
Category = 'category'  # str
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

columnList = ['ID', 'FirstName', 'LastName', 'Phone', 'Email', 'AppointmentDate', 'Canceled', 'CanClientCancel']

columnsDict = {'ID': ID, 'FirstName':  FirstName, 'LastName': LastName, 'Phone': Phone, 'Email': Email,
               'AppointmentDate': Date, 'Canceled': Cancelled, 'CanClientCancel': CanClientCancel}


def insert_appointment_scheduling_data(api_data):
    print(len(api_data))
    sql_query = ''
    no_of_rows = 0
    list_of_rows = []
    for item in api_data:
        sql_query_cols = 'Insert into appointmentScheduling1 ('
        no_of_col = 0
        for col_name in columnList:
            if no_of_col < len(columnList) - 1:
                sql_query_cols += col_name + ', '
            else:
                sql_query_cols += col_name + ') values ('
            no_of_col += 1
        sql_query = "\n" + sql_query_cols
        # print(sql_query_cols)
        no_of_col = 0
        for col_name in columnList:
            if no_of_col < len(columnList) - 1:
                if type(item[columnsDict[col_name]]) is str:
                    sql_query += "'" + item[columnsDict[col_name]] + "',"
                elif type(item[columnsDict[col_name]]) is int:
                    sql_query += str(item[columnsDict[col_name]]) + ","
                elif type(item[columnsDict[col_name]]) is bool:
                        sql_query += str(item[columnsDict[col_name]]) + ","
            else:
                if type(item[columnsDict[col_name]]) is str:
                    sql_query += "'" + item[columnsDict[col_name]] + "' )"
                elif type(item[columnsDict[col_name]]) is int:
                    sql_query += str(item[columnsDict[col_name]]) + ')'
                elif type(item[columnsDict[col_name]]) is bool:
                        sql_query += str(item[columnsDict[col_name]]) + " ) "
            no_of_rows += 1
            no_of_col += 1
        sql_query += ';'
        print(sql_query)
        my_cursor.execute(sql_query)
        # my_db.commit()
    # print('The no of rows inserting are ' + str(no_of_rows))
    # print(sql_query)



insert_appointment_scheduling_data(response1.json())
my_db.commit()





