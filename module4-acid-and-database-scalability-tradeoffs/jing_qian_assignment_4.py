"""
Because the first n questions are so easy, only sql script is shown
We'll focus on the bonus question
"""
"""
# How many passengers survived, and how many died?
SELECT COUNT(name) FROM titanic
GROUP BY survived 

#How many passengers were in each class?
SELECT COUNT(name) FROM titanic 
GROUP BY pclass
ORDER BY pclass

#How many passengers survived/died within each class?
SELECT COUNT(name) FROM titanic
GROUP BY survived 
GROUP BY pclass

#What was the average age of survivors vs nonsurvivors?
SELECT AVG(age) FROM titanic
GROUP BY survived 

#What was the average age of each passenger class?
SELECT AVG(age) FROM titanic
GROUP BY pclass

#What was the average fare by passenger class? By survival?
SELECT AVG(fare) FROM titanic
GROUP BY survived

#How many siblings/spouses aboard on average, by passenger class? By survival?
SELECT  AVG(siblings_spouses_aboard) FROM titanic
GROUP BY pclass

SELECT  AVG(siblings_spouses_aboard) FROM titanic
GROUP BY survived

#How many parents/children aboard on average, by passenger class? By survival?
SELECT  AVG(parents_children_aboard) FROM titanic
GROUP BY pclass

SELECT  AVG(parents_children_aboard) FROM titanic
GROUP BY survived

#Do any passengers have the same name?
SELECT survivor_id, name, COUNT(*) FROM titanic
GROUP BY name
HAVING COUNT(*)>1
"""
#(Bonus! Hard, may require pulling and processing with Python) How many married couples were aboard the Titanic? Assume that two people(one Mr. and one Mrs.) with the same last name and with at least 1 sibling/spouse aboard are a married couple.
import pandas as pd
import numpy as np
filename = "/Users/jing/Documents/LambdaSchool/LS_DS_unit3/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv"
df = pd.read_csv("titanic.csv")
print(df.head(5))

#get_statement = """
#SELECT 
