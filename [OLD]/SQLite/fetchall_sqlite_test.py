from datetime import datetime
import json
import os
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError
import sqlite3
import time
from tqdm import tqdm

url = 'https://e621.net/posts.json?limit=320'
e621_agent = {
   'User-Agent': 'Training Dataset (EKrabs)',
   'login': 'EKrabs',
   'api_key': '7yqTWqrn1CLk4nG6q4J1W6s4'
}

login = 'EKrabs' # your username
api_key = '7yqTWqrn1CLk4nG6q4J1W6s4' # your api key

request_count = 0
seen = {}
cwd = os.getcwd()
y = datetime.now().year
m = datetime.now().month
d = datetime.now().day
columns = ['id', 'created_at', 'updated_at', 'file', 'preview', 'sample', 
	'score', 'tags', 'locked_tags', 'change_seq', 'flags', 'rating', 'fav_count',
	'sources', 'pools', 'relationships', 'approver_id', 'uploader_id', 'description',
	'comment_count', 'is_favorited', 'has_notes', 'duration']

db = sqlite3.connect(f'{cwd}/e621-total-{y}-{m}-{d}.sqlite')
c = db.cursor() 
c.execute('CREATE TABLE IF NOT EXISTS e621 ({})'.format(' text,'.join(columns)))
c.execute('DELETE FROM e621')

def insert_sqlite(values):
	insert_query = 'INSERT INTO e621 ({}) VALUES (?{})'.format(','.join(columns), ',?'*(len(columns)-1))
	c.executemany(insert_query, values)
	db.commit() #commit every time instead of bulk incase of failure

def get_start_id():
	try:
		r = requests.get(url, headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
	except ConnectionError as e: #not the built in one
		print(e)
		exit()
	if r.status_code != 200:
		print(r.status_code)
		exit()

	data = r.json()
	return data['posts'][0]['id']

start_id = get_start_id()

with tqdm(total=(start_id/320)+1) as pbar:
	while True:
		try:
			r = requests.get(f'{url}&page=b{start_id}', headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
		except requests.exceptions.ConnectionError as e:
			print('\n'+str(e))
			time.sleep(60)
			continue
		if r.status_code != 200:
			print('\n'+str(r.status_code))
			time.sleep(60)
			continue

		s = time.time()
		data = r.json()
		value = []
		values = []
		for post in data['posts']:
			md5 = post['file']['md5']
			if md5 in seen:
				continue
			seen[md5] = 1
			for column in columns:
				value.append(json.dumps(dict(post).get(column)))
			values.append(list(value))
			value.clear()

		if len(values) == 0:
			break

		insert_sqlite(values)
		time.sleep(2-(time.time()-s))
		pbar.update(1)
		request_count += 1
		start_id -= 320

c.close()
print(f'\nFetched {len(seen)} records, with {request_count+1} requests')
