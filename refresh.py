import requests
from requests.auth import HTTPBasicAuth
import time
import json
import sqlite3

from datetime import datetime
import os

url = 'https://e621.net/posts.json?limit=320'
e621_agent = {
	'User-Agent': 'TagData (by EKrabs)',
	'login': 'EKrabs',
	'api_key': '7yqTWqrn1CLk4nG6q4J1W6s4'
}

login = 'EKrabs' # your username
api_key = '7yqTWqrn1CLk4nG6q4J1W6s4' # your api key

max_id =  #3138380
seen = {} #[]
run = 1
cwd = os.getcwd()

for fname in os.listdir('.'):
	if fname.endswith('.sqlite') == True:
		sqlite_file = cwd + '\\' + fname
		break
else:
	print('Please generate the database.')
	exit()

start = time.time()
with open(f'{cwd}\\e621-refresh.json', 'w') as f:

	f.write('[')
	while True:
		while_start = time.time()

		r = requests.get(f'{url}&page=a{max_id}', headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
		if r.status_code != 200:
			print(r.status_code)
			time.sleep(15)
			continue

		data = r.json()
		for index, item in enumerate(data['posts']):
			post_id = item['id']
			md5 = item['file']['md5']

			if md5 in seen:
				continue
			seen[md5] = 1
			#seen.append(item['file']['md5'])
			print('{}'.format(post_id))
			f.write(json.dumps(item)) #+ '\n'

			if index+1 != len(data['posts']):
				f.write(',')

		time.sleep(2)
		now = time.time()
		if now-while_start <= 2:
			break
		print(f'Loop {run}: {now-while_start}')
		max_id += 320
		run += 1
	f.write(']')
now = time.time()
print(f'Fetched {len(seen)} records, with {run-1} requests in {now-start}')

print(f'Connecting to {sqlite_file}')
db = sqlite3.connect(sqlite_file)
print('Converting')
with open(f'{cwd}\\e621-refresh.json', encoding='utf-8') as f:
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
	print('Inserting')
	create_query = 'create table if not exists myTable ({0})'.format(' text,'.join(columns))
	insert_query = 'insert into myTable ({0}) values (?{1})'.format(','.join(columns), ',?' * (len(columns)-1))    
	print("Insert has started at " + str(datetime.now()))  
	c = db.cursor()   
	c.execute(create_query)
	c.executemany(insert_query , values)
	print('Sorting by ID')
	c.execute('SELECT * FROM myTable ORDER BY CAST(id AS INT)')
	values.clear()
	db.commit()
	c.close()
now = time.time()
print(f'Insert has completed at {datetime.now()} in {now-start}' + str(datetime.now()))
