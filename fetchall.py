from datetime import datetime
import json
import os
import requests
from requests.auth import HTTPBasicAuth
import sqlite3
import time
from tqdm import tqdm

url = 'https://e621.net/posts.json?limit=320'
e621_agent = {
   'User-Agent': 'TagData (by )',
   'login': '',
   'api_key': ''
}

login = '' # your username
api_key = '' # your api key

request_count = 0
seen = {}
cwd = os.getcwd()
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
columns = ['id', 'created_at', 'updated_at', 'file', 'preview', 'sample', 
	'score', 'tags', 'locked_tags', 'change_seq', 'flags', 'rating', 'fav_count',
	'sources', 'pools', 'relationships', 'approver_id', 'uploader_id', 'description',
	'comment_count', 'is_favorited', 'has_notes', 'duration']

db = sqlite3.connect('{}/e621-total-{}-{}-{}.sqlite'.format(cwd, year, month, day))
c = db.cursor() 
c.execute('CREATE TABLE IF NOT EXISTS e621 ({})'.format(' text,'.join(columns)))
c.execute('DELETE FROM e621')

def insert_sqlite(values):
	insert_query = 'INSERT INTO e621 ({}) VALUES (?{})'.format(','.join(columns), ',?'*(len(columns)-1))
	c.executemany(insert_query, values)

def get_start_id():
	try:
		r = requests.get(url, headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
	except Exception as e:
		print(e)
		exit()
	if r.status_code != 200:
		print(r.status_code)
		exit()

	data = r.json()
	return data['posts'][0]['id']

start_id = get_start_id()
print(start_id)
with tqdm(total=start_id/320+1) as pbar:
	while True:
		try:
			r = requests.get('{}&page=b{}'.format(url, start_id), headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
		except Exception as e:
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
			#_id = post['id']
			md5 = post['file']['md5']
			if md5 in seen:
				continue
			seen[md5] = 1
			#print(_id)
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

db.commit()
c.close()
print('\nfetched {} records, with {} requests'.format(len(seen), request_count+1))
