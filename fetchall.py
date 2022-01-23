import requests
from requests.auth import HTTPBasicAuth
import time
import json
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

max_id = 3138380 #3138380 3011069 3053317 3011070 2992268 518808
seen = {} #[]
run = 1
directory = 'C:/Scripts/Python/e621-json-dump-main/'
''' When refreshing data, change 'w' to 'a' '''
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
with open('{}JSON/e621-total-{}-{}-{}-a.json'.format(directory, year, month, day), 'w') as f:
	''' When refreshing data, replace f.write('[') to (',') '''
	f.write('[')
	while True:
		while_start = time.time()
		''' When refreshing data, change page=b{} to page=a{} '''
		r = requests.get('{}&page=b{}'.format(url, max_id), headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
		#print('{}&page=b{}'.format(url, max_id))
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
			if index != len(data['posts']) - 1:
				f.write(',')
		''' When refreshing data, change -= 320 to += 320 '''
		time.sleep(2)
		now = time.time()
		if now-while_start < 3:
			break
		print('Loop {}: {}'.format(run, now-while_start))
		max_id -= 320
		run += 1
	f.write(']')

print('Fetched {} records, with {} requests'.format(len(seen), run-1))
