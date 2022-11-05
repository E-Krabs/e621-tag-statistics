import json
import sqlite3
from datetime import datetime

# https://www.codeproject.com/Tips/4067936/Load-JSON-File-with-Array-of-Objects-to-SQLite3-On
directory = 'C:/Scripts/Python/e621-json-dump-main'
db = sqlite3.connect('{}/JSON/jsql.sqlite'.format(directory))
with open('{}/JSON/e621-total-2021-11-05-a.json'.format(directory), encoding='utf-8') as f:
	json_data = json.loads(f.read())
	
#Aim of this block is to get the list of the columns in the JSON file.
	columns = []
	column = []
	for data in json_data:
		column = list(data.keys())
		for col in column:
			if col not in columns:
				columns.append(col)
								
#Here we get values of the columns in the JSON file in the right order.   
	value = []
	values = [] 
	for data in json_data:
		for i in columns:
			value.append(json.dumps(dict(data).get(i)))#IMPORTANT 
		values.append(list(value)) 
		value.clear()
		
#Time to generate the create and insert queries and apply it to the sqlite3 database       
	create_query = "create table if not exists myTable ({0})".format(" text,".join(columns))
	insert_query = "insert into myTable ({0}) values (?{1})".format(",".join(columns), ",?" * (len(columns)-1))    
	print("insert has started at " + str(datetime.now()))  
	c = db.cursor()   
	c.execute(create_query)
	c.executemany(insert_query , values)
	values.clear()
	db.commit()
	c.close()
	print("insert has completed at " + str(datetime.now()))