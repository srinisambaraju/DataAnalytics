import requests
import mysql.connector

# The below is for connecting to mySQL, use your login and password and the database name
# see the declaration below, replace the values inside the angled brackets
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="!Ramani@72",
    database="acuityscheduling"
)
mindate = "02/01/2019"
maxdate = "02/02/2019"
my_cursor = my_db.cursor()
url = "https://acuityscheduling.com/api/v1/appointments"
querystring = {"minDate": mindate, "maxDate": maxdate}
payload = ""
headers = {
    'Authorization': "Basic MTcwNDI5NjM6ZTEyYzQ3YWJlMDNjMDI0OGY0MzllNjgyZWQyMjgzMzA=",
    'cache-control': "no-cache",
    'Postman-Token': "95d7e05b-22f2-4ecd-b967-17251b5c3633"

    }
# The below is the response object from Acuity, the data is sometimes wrong for example in some cases the Phone no has
# email and email has the phone no, you need to talk to Acuity to correct or the Reps who are entering the data
# to enter it properly
response1 = requests.request("GET", url, data=payload, headers=headers, params=querystring)

columnList = ['id', 'firstName', 'lastName', 'phone', 'email', 'date', 'canceled', 'canClientCancel']

sql_query = 'Insert into appointmentScheduling1 ('


sql_insert_query = 'Insert into appointmentScheduling1 (ID, FirstName, LastName, Phone, Email, AppointmentDate, ' \
                    'Canceled, CanClientCancel) values (%s, %s, %s, %s, %s, %s, %s, %s)'

# This is the actual column list that matches the DB columns created as part of SQL Script, see the names of the columns
# I created are matching the variable columnList. I am using that columnList to loop through to create sQl query
# The below script is used to create the table in mysql, you can add columns you like
# CREATE TABLE appointmentScheduling1 (
#   ID bigint NOT NULL,
#   FirstName varchar(35) NOT NULL,
#   LastName varchar(35) NOT NULL,
#   Email varchar(50) NOT NULL,
#   Phone varchar(50) NULL,
#   Canceled bit Null,
#   CanClientCancel bit NULL,
#   AppointmentDate varchar(50) NULL,
#   PRIMARY KEY (ID)
#   );

# Column list is created which matches the db column names as you can see above


def insert_appointment_scheduling_data(api_data):
    row_data = []
    # THe below is to loop through the Json output coming from the API
    # The below loop is going through the columns list declared above to add the column names to the sql_query_cols
    for item in api_data:
        # Creating the Insert statement
        # The below loop is going through the column list again and trying to fetch the value
        # sql_query += '( '
        row_tuple = ()
        for col_name in columnList:
            row_tuple += (item[col_name],)
        row_data.append(row_tuple)
    return row_data

# Function is returning tuple values which can be used to insert bulk data into the DB


row_data_values = insert_appointment_scheduling_data(response1.json())
my_cursor.executemany(sql_insert_query, row_data_values)
my_db.commit()
print(str(len(response1.json())) + ' rows of data is inserted into the database successfully')
