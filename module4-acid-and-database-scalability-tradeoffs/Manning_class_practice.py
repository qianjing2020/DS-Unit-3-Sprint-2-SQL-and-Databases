import os
from os import getcwd
import sys

sys.path.append(getcwd())

import sqlite3
conn = sqlite3.connect('Thursday.sqlite')
cur = conn.cursor()
# when creating table, use NOT NULL to prevent an empty cell
# don't run create table after the table has been created!

# cur.execute('''
# CREATE TABLE SCHOOL
# (ID INT PRIMARY KEY NOT NULL,  
# NAME TEXT NOT NULL,
# AGE INT NOT NULL,
# ADDRESS CHAR(50),
# MARKS INT);''') 


# # insert
# cur.execute("""INSERT INTO SCHOOL (ID, NAME, AGE, ADDRESS, MARKS)\
#     VALUES (1, 'Rohan', 14, 'Delhi', 200)""")
# cur.execute("INSERT INTO SCHOOL (ID, NAME, AGE, ADDRESS, MARKS)\
#     VALUES (2, 'Lisa', 13, 'Kolkata', 250)")
# cur.execute("INSERT INTO SCHOOL (ID, NAME, AGE, ADDRESS, MARKS)\
#     VALUES (3, 'Allen', 12, 'Hyderabad', 600)")
# conn.commit()

# print to check
for row in cur.execute("SELECT ID, NAME, MARKS FROM SCHOOL"):
    print('ID = ', row[0])
    print('NAME = ', row[1])
    print('MARKS =', row[2], '\n')
conn.commit()

# update
# also as shown here: sql is not case-sensitive, so it's personal choice to keep query keys capitalzied, capital letter is for better readability
cur.execute("update school set marks = 900 where id = 1") 
conn.commit()

# print to check the update
for row in cur.execute("SELECT ID, NAME, MARKS FROM SCHOOL"):
    print('ID = ', row[0])
    print('NAME = ', row[1])
    print('MARKS =', row[2], '\n')
conn.commit()

conn.close()