import os
import urllib.parse as up
import os
from os import getcwd
import sys

sys.path.append(getcwd())
#sys.path.append("/usr/bin/")
#sys.path.append("/usr/local/lib/python3.7/site-packages/")
import psycopg2

# method 1 to connect
up.uses_netloc.append("postgres")
DATABASE_URL = "postgres://fekuuytp:08RQSNoiKG1C32Nwg18VkHcblP_-z_hD@rajje.db.elephantsql.com:5432/fekuuytp"
url = up.urlparse(DATABASE_URL)
try:
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=str(url.port),
    )
except:
    print("Elephant: I am not able to connect to the database.")

# create cursor object
cur = conn.cursor()

# get the total number of rows
cur.execute("""SELECT COUNT(*) FROM charactercreator_character""")
print(cur.fetchall())

# get all rows
cur.execute("""SELECT * FROM charactercreator_character""")
rows = cur.fetchall()
# print each row and its columns values
for row in rows:
    print('character_id', row[0])
    print('name', row[1])
    print('level', row[2])
    print('exp', row[3])
    print('hp', row[4])
    print('strength', row[5])
    print('intelligence', row[6])
    print('dexterity', row[7])
    print('wisdom', row[8])
