import os
import requests
from requests.auth import HTTPBasicAuth
import time
import json
from datetime import datetime
import sqlite3

url = 'https://e621.net/posts.json?limit=320'
e621_agent = {
   'User-Agent': 'TagData (by )',
   'login': '',
   'api_key': ''
}

login = '' # your username
api_key = '' # your api key

start_id = 0
seen = {}
run = 1
cwd = os.getcwd()
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
columns = ['id', 'created_at', 'updated_at', 'file', 'preview', 'sample', 
	'score', 'tags', 'locked_tags', 'change_seq', 'flags', 'rating', 'fav_count'
	'sources', 'pools', 'relationships', 'approver_id', 'uploader_id', 'description'
	'comment_count', 'is_favorited', 'has_notes', 'duration']

db = sqlite3.connect('{}/e621-total-{}-{}-{}.sqlite'.format(cwd, year, month, day))
c = db.cursor() 
c.execute('CREATE TABLE if not exists e621 ({})'.format(' text,'.join(columns)))

def insert_sqlite(values):
	insert_query = 'INSERT INTO e621 ({}) VALUES (?{})'.format(','.join(columns), ',?'*(len(columns)-1))
	c.executemany(insert_query, values)

while True:
	time_start = time.time()
	r = requests.get('{}&page=a{}'.format(url, start_id), headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
	if r.status_code != 200:
		print(r.status_code)
		time.sleep(15)
		continue

	data = r.json()
	value = []
	values = []
	for post in data['posts']:
		_id = post['id']
		md5 = post['file']['md5']
		if md5 in seen:
			continue
		seen[md5] = 1
		print(_id)
		for item in columns:
			value.append(json.dumps(dict(post).get(item)))
		values.append(list(value))
		value.clear()

	if len(values) == 0:
		break

	insert_sqlite(values)
	time.sleep(2)
	time_now = time.time()
	print('loop {}: {}'.format(run, time_now-time_start))
	start_id += 320
	run += 1

db.commit()
c.close()
print('fetched {} records, with {} requests'.format(len(seen), run-1))
