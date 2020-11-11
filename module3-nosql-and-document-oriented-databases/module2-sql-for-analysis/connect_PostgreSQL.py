import urllib.parse as up
import psycopg2
def connect_postgresql(db_url):
    # connect to elephantsql
    up.uses_netloc.append("postgres")
    DATABASE_URL = db_url
    url = up.urlparse(DATABASE_URL)
    try:
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=str(url.port),
        )
        cur = conn.cursor()
    except:
        print("Elephant: I am not able to connect to the database.")
    return conn, cur

