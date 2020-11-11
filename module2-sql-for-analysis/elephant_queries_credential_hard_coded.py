import psycopg2

## Credentials to elephantSQL -hosted PostgreSQL
"""dbname = "fekuuytp"
user = "fekuuytp"
password = "08RQSNoiKG1C32Nwg18VkHcblP_-z_hD"
host = "rajje.db.elephantsql.com"
"""
dbname = "owxkzuqy"
user = "owxkzuqy"
password = "oPE6Y8aiCDPKQZO23z-g8IZiKm1HK8O2"
host = "otto.db.elephantsql.com"

### Connect to ElephantSQL
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()

### Note different from sqlite: we can do result=cur.excecute(query).fetchall()
# but in psycopg, it is a two step process: curson execute query first then fetch
cur.execute('SELECT * from test_table;')

result = cur.fetchall()
print(result)