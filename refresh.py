import requests
from requests.auth import HTTPBasicAuth
import time
import json
import sqlite3

from datetime import datetime
import os

url = 'https://e621.net/posts.json?limit=320'
e621_agent = {
	'User-Agent': 'TagData (by )',
	'login': '',
	'api_key': ''
}

login = '' # your username
api_key = '' # your api key

max_id = 3143512 #3138380 3011070 2992268 518808
seen = {} #[]
run = 1
directory = 'C:/Scripts/Python/e621-json-dump-main'
''' When refreshing data, change 'w' to 'a' '''
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
with open('{}/JSON/e621-refresh.json'.format(directory, year, month, day), 'w') as f:
	''' When refreshing data, replace f.write('[') to (',') '''
	f.write('[')
	while True:
		while_start = time.time()
		''' When refreshing data, change page=b{} to page=a{} '''
		r = requests.get('{}&page=a{}'.format(url, max_id), headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
		if r.status_code != 200:
			print(r.status_code)
			time.sleep(15)
			continue

		data = r.json()
		for index, item in enumerate(data['posts']):
			post_id = item['id']
			md5 = item['file']['md5']
			''' Check if image was already indexed by comparing md5 '''
			if md5 in seen:
				continue
			seen[md5] = 1
			#seen.append(item['file']['md5'])
			print('{}'.format(post_id))
			f.write(json.dumps(item)) #+ '\n'
			''' Don't write a comma on the last post '''
			if index+1 != len(data['posts']):
				f.write(',')
		''' When refreshing data, change -= 320 to += 320 '''
		time.sleep(2)
		now = time.time()
		if now-while_start < 3:
			break
		print('Loop {}: {}'.format(run, now-while_start))
		max_id += 320
		run += 1
	f.write(']')
print('Fetched {} records, with {} requests'.format(len(seen), run-1))

db = sqlite3.connect('{}/JSON/jsql.sqlite'.format(directory))
with open('{}/JSON/e621-refresh.json'.format(directory), encoding='utf-8') as f:
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
			value.append(str(dict(data).get(i)))   
		values.append(list(value)) 
		value.clear()
		
#Time to generate the create and insert queries and apply it to the sqlite3 database       
	create_query = 'create table if not exists myTable ({0})'.format(' text,'.join(columns))
	insert_query = 'insert into myTable ({0}) values (?{1})'.format(','.join(columns), ',?' * (len(columns)-1))    
	print("Insert has started at " + str(datetime.now()))  
	c = db.cursor()   
	c.execute(create_query)
	c.executemany(insert_query , values)
	db.commit()
	c.execute('SELECT * FROM myTable ORDER BY CAST(id AS INT)')
	values.clear()
	db.commit()
	c.close()
print('Insert has completed at ' + str(datetime.now()))


