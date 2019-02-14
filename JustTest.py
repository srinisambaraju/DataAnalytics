import numpy as np

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

sql_query = 'Insert into appointmentScheduling1 ('
col_tuple = ()
for col in columnList:
    col_tuple += '\'' + col + '\''

    # col_tuple += col
print(col_tuple)
