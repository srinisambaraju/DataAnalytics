import pandas as pd
import seaborn as sns
sns.set()

new_file = pd.ExcelFile(r'C:\Srini\AR_BillCredits_Summary_Detail.xls')



# raw_data = pd.read_excel(r'C:\Srini\AR_BillCredits_Summary_Detail.xlsx', header=[3, 4], sheet_name='Wireless Reviewed Bill Credits')

raw_data = new_file.parse('Wireless Reviewed Bill Credits', skiprows=3)

# print(raw_data)
# print(raw_data.columns)

x = raw_data.iloc[:, 1:]
#
# # x = data.iloc[:, 1:]
#
# print(x)
#
# print(x.columns)
# print(x)
#
# print(type(raw_data))
print(type(x))
print('The number of rows in the spread sheet are {}'.format(x.shape[0]))
print('The number of columns in the spread sheet are {}'.format(x.shape[1]))
print(x.columns)
x.drop(x.columns[x.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
print(x.columns)
# print(raw_data.dtypes)
print(type(x.shape[0]))
print(x)


# for row in range(x.shape[0]):
#     # for col in range(x.shape[1]):
#     #     t = x.iloc[row, col]
#     row_data = x.iloc[row:row+1, 0:]
#     print(row_data)
# print('the loop is done')

