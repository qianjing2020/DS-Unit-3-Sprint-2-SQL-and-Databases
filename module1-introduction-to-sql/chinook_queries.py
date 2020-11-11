import os
import sqlite3

filename = "chinook.db"
# file_path = "module1-introduction-to-sql/chinook.db"
# Best practice: Let os module detrmines where to find the file and for path which slash works slash(mac) or backslash (windows) 
file_path = os.path.join(os.path.dirname(__file__),"..", filename)

# print(__file__)
print("file", __file__)

print("file path", file_path)

breakpoint()
conn = sqlite3.connect(file_path)
print("connection", conn)

cur = conn.cursor()
print("cursor", cur)

query = "SELECT * FROM customers;"

result = cur.execute(query).fetchall()

# print(result)

# print(type(result), type(result[0]))

for row in result:
    print(row)