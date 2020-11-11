""" README.md in correspondent github repository
Part 1
"""
import sys
from os import getcwd

mywd = getcwd()
sys.path.append(mywd)
"""import wget 
# get data
url = 'https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true'
filename = wget.download(url) 
"""
filename = "rpg_db.sqlite3"
import sqlite3

conn = sqlite3.connect(filename)
curs = conn.cursor()
# How many total Characters are there?
get_counts = "SELECT COUNT(*) FROM charactercreator_character"
character_counts = curs.execute(get_counts).fetchall()
# Extract characters
get_characters = "SELECT * FROM charactercreator_character"
characters = curs.execute(get_characters).fetchall

# find the total number of items in armory_item table
get_counts = "SELECT COUNT(item_id) FROM armory_item"
get_armory_item = "SELECT * FROM armory_item"
get_armory_weapon = "SELECT * FROM armory_weapon"

armory_counts = curs.execute(get_counts).fetchall()
armory_items = curs.execute(get_armory_item).fetchall()
armory_weapon = curs.execute(get_armory_weapon).fetchall()

count_weapon = len(armory_weapon)
count_armory = len(armory_items)
count_non_weapon = count_armory - count_weapon
# curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()
""" instead of using math, we can also query directly:
method1:
SELECT COUNT(DISTINCT item_id) FROM armory_item
WHERE item_id NOT IN (SELECT item_ptr_id FROM armory weapon)
method2:
SELECT COUNT(DISTINCT item_id)-COUNT(DISTINCT item_ptr_id)
FROM armory_item, armory_weapon
"""

# How many Items does each character have? (Return first 20 rows)
get_item_count_per_character = """
SELECT COUNT(character_id), item_id 
FROM charactercreator_character_inventory 
GROUP BY item_id 
ORDER BY COUNT(character_id) DESC
LIMIT 20
"""
item_count_per_character = curs.execute(get_item_count_per_character).fetchall()

# How many Weapons does each character have? (Return first 20 rows)
get_weapon_count_per_character = """
SELECT COUNT(character_id), character_id, item_id 
FROM charactercreator_character_inventory
INNER JOIN armory_weapon 
ON armory_weapon.item_ptr_id=charactercreator_character_inventory.item_id
GROUP BY item_id
LIMIT 20
"""
weapon_count_per_character = curs.execute(get_weapon_count_per_character).fetchall()

# On average, how many Items does each Character have?
sum_item = [lis[0] for lis in item_count_per_character]
avg_item_per_character = sum(sum_item) / len(item_count_per_character)
avg_item_per_character

# On average, how many Weapons does each Character have?
sum_weapon = [lis[0] for lis in weapon_count_per_character]
avg_weapon_per_character = sum(sum_weapon) / len(weapon_count_per_character)
avg_weapon_per_character

conn.close()


""" 
Part 2 
"""
import pandas as pd

df = pd.read_csv("buddymove_holidayiq.csv")
print(df.dtypes)
conn = sqlite.connect()
curs = conn.cursor()
# Create table
db_file = "buddymove_holidayiq.sqlite3"
table_1 = "table_1"
# curs.execute('CREATE TABLE {tn}'\
#    .format(tn=table_1)
