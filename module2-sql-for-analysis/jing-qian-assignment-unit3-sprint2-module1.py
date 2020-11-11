# how many of the items are weapons?
select 
 sum(w.item_ptr_id is null) as non_weapon_count
 ,sum(w.item_ptr_id is not null) as weapon_count
from armory_item i 
left join armory_weapon w on i.item_id = w.item_ptr_id

# How many Weapons does each character have? (Return first 20 rows)
# assume: also count 0 for char that don't have weapons
# 302 rows (characters)
SELECT
  c.character_id
  ,c.name as char_name
  ,count(inv.item_id) as item_count
  ,count(w.item_ptr_id) as weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
GROUP BY c.character_id # row per what?
ORDER BY weapon_count DESC
# LIMIT 20
SELECT * from 