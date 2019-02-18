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

# This is the DB script for Stores

# CREATE TABLE stores (
#     StoreId MEDIUMINT NOT NULL,
#     StoreName varchar(100) Null,
#     LocationEntityID BIGINT NOT NULL,
#     PRIMARY KEY (StoreId)
# );

# Function to retrieve the details of the various stores and store it in the DB, currently we are not using the data
# in that table


def insert_store_data_into_stores_table():
    url_for_stores = "https://dataconnect.iqmetrix.net/lists/stores"
    url_for_stores = "https://dataconnect.iqmetrix.net/reports/locationmasterlistreport"
    payload = ""

    response = requests.request("GET", url_for_stores, data=payload, headers=headers)
    stores_column_list = ['StoreID', 'StoreName', 'LocationEntityID']

    store_insert_query = 'Insert into stores ( StoreId, StoreName, LocationEntityId) Values ( %s, %s, %s )'
    row_data = []
    store_id_values = []
    for store in response.json():
        sql_fetch = 'Select * from Stores where StoreId = ' + str(store['StoreID'])
        my_cursor.execute(sql_fetch)
        records = my_cursor.fetchall()
        store_id_values.append(store['StoreID'])
        if int(my_cursor.rowcount) > 0:
            print("There is a store with this Id already exists" + str(store['StoreID']))
            continue
        store_row_tuple = ()

        for column in stores_column_list:
            print()
            print('Store Id {} Store Name {} LocationEntityID {}'.format(store['StoreID'], store['StoreName'],
                                                                         store['LocationEntityID']))

            store_row_tuple += (store[column],)
        row_data.append(store_row_tuple)
        #  if type(item[columnsDict[col_name]]) is str:
    print(row_data)
    my_cursor.executemany(store_insert_query, row_data)
    my_db.commit()
    return store_id_values, len(row_data)

# Function to retrieve the details of the districts for which we need to pull the inventory data


def get_district_ids():

    # region Details needed for District ID's

    url = "https://dataconnect.iqmetrix.net/lists/LocationIDs"
    querystring = {"LocationType": "District", "LocationTypeIDs": "", "LanguageCode": ""}
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    # endregion
    district_list = []
    print(len(response.json()))
    for district_obj in response.json():
        district_list.append(district_obj['ID'])
    return district_list

# Function to retrieve the inventory product list for individual districts


def get_inventory_product_list_for_individual_districts(district_id):

    # CREATE TABLE inventorylistinstores (
    #   DistrictName varchar(100) NOT NULL,
    #   RegionName varchar(50) NOT NULL,
    #   ChannelName varchar(50) NOT NULL,
    #   WriteOff binary NULL,
    #   NoSale binary NULL,
    #   VendorPartNumber varchar(100) NULL,
    #   ManufacturerPartNumber varchar(100) NULL,
    #   DiscontinuedDate date NULL,
    #   BinStatus varchar(50) NULL,
    #   Quantity mediumint NULL,
    #   SerialNumber varchar(50) NULL,
    #   StoreTypeName varchar(100) NOT NULL,
    #   DoNotOrder binary NULL,
    #   DateEOL date NULL,
    #   IsUsed  binary NULL,
    #   SpecialOrder binary NULL,
    #   ProductIdentifier varchar(100) NULL,
    #   TotalCost float NULL,
    #   ProductName varchar(100) NULL,
    #   StoreName varchar(100) NULL,
    #   VendorName varchar(100) NULL,
    #   UnitCost float NULL,
    #   CategoryPath varchar(10000) NULL,
    #   WarehouseLocation varchar(100) NULL,
    #   RefundPeriodLength int NULL,
    #   BarCode varchar(10000) NULL
    #   )

    # region Details of the inventory rest api call
    url_for_inventory = 'https://dataconnect.iqmetrix.net/reports/inventorylistingreport'
    payload1 = ""

    querystring = {"LanguageCode": "", "LocationTypeIDs": str(district_id), "LocationType": "District",
                   "BinStatus": "10", "QtyStatus": "4", "BlindInventory": "", "CategoryNumber": ""}
    inventory_response = requests.request("GET", url_for_inventory, data=payload1, headers=headers, params=querystring)

    #endregion

    # Below is the list of columns that you need to pull the value from Json output so the data can be inserted
    # into the database
    inventory_list_columns = ['DistrictName', 'RegionName', 'ChannelName', 'WriteOff', 'NoSale', 'VendorPartNumber',
                              'ManufacturerPartNumber', 'DiscontinuedDate', 'BinStatus', 'Quantity', 'SerialNumber',
                              'StoreTypeName', 'DoNotOrder', 'DateEOL', 'IsUsed', 'SpecialOrder', 'ProductIdentifier',
                              'TotalCost', 'ProductName', 'StoreName', 'VendorName', 'UnitCost', 'CategoryPath',
                              'WarehouseLocation', 'RefundPeriodLength', 'BarCode']
    # This is the query that would insert the data and the values are going to be filled later on while looping through
    # the output
    insert_inventory_query = 'Insert into inventorylistinstores (DistrictName, RegionName, ChannelName, WriteOff, ' \
                             'NoSale, VendorPartNumber, ManufacturerPartNumber, DiscontinuedDate, BinStatus, ' \
                             'Quantity, SerialNumber,StoreTypeName, DoNotOrder, DateEOL, IsUsed, SpecialOrder, ' \
                             'ProductIdentifier, TotalCost, ProductName, StoreName, VendorName, UnitCost, ' \
                             'CategoryPath, WarehouseLocation, RefundPeriodLength, BarCode) values ( ' \
                             '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,' \
                             '%s, %s, %s, %s )'
    row_data = []
    print('The no of rows that exists for this district {} are {}'.format(district_id,
                                                                          len(inventory_response.json())))
    total_row_count = 0
    row_count = 0
    # The below for loop is to loop through all the inventory items that are in a specific district
    for inventory_item in inventory_response.json():
        inventory_data_tuple = ()
        row_count += 1
        total_row_count += 1
        # The below loop is to loop each and every row of the json output and prepare it for inserting it into DB
        # Used a tuple to store each column value and then added that to a list which is used to store bulk data
        # at once into the DB
        for inventory_column in inventory_list_columns:
            inventory_data_tuple += (inventory_item[inventory_column],)
        # All the column data of a row is in the tuple inventory_data_tuple which is then appended to the row_data
        row_data.append(inventory_data_tuple)
        # The condition below is added because mysql has a limitation towards inserting more than specific rows at
        # a time, I couldn't find what's that limit, so for now I set it to 1000 and I can insert 1000 at a time
        # without any issues
        # Once the 1000 rows are inserted the main loop which has more than 1000 is still going, so we need to
        # initialize the row_data so we don't insert that again, so initialised the row_data again to nothing
        if row_count > 1000:
            my_cursor.executemany(insert_inventory_query, row_data)
            my_db.commit()
            # Had to re-initialize again back to empty, so we can add new data and also initializing the count as well
            # to 0, so we can use that condition to check
            row_data = []
            row_count = 0
    # Still returning the remaining rows back so we can do the commit, for ex: In the first iteration
    # we inserted 1000, but they are a total of 1234 rows that json output is giving us. The loop will still
    # continue and store the remaining data of 234 in the row_data which are not going to be inserted into the db
    # because we are saying if the row_count is > 1000 go and insert them, so what I am doing is sending these 234 rows
    # back to the function from where it is being called and inserting it there. After that we are calling the function
    # again to insert the data for the next district
    # json output, so 1000 will be inserted and
    print('The total number of rows inserted for the district {} are {}'.format(district_id, total_row_count))
    return insert_inventory_query, row_data

# The below function is retrieving the stores data from the api which is not taking into account of active stores
# There is a different API for it which we need to call and store that data


store_id_values, row_count = insert_store_data_into_stores_table()
# The below function retrieves the data for various districts and stores them in a list. The same list will be used
# to loop through those and get the inventory for each of those districts
district_id_values = get_district_ids()

# The below loop is going through those various districts and get's the inventory and stores them in the DB
for district in district_id_values:
    insert_query, inventory_row_data = get_inventory_product_list_for_individual_districts(str(district))
    # The below statement is going to insert the left out rows that we did not insert above
    my_cursor.executemany(insert_query, inventory_row_data)
    my_db.commit()

