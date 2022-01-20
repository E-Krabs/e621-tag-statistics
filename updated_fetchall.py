import requests
from requests.auth import HTTPBasicAuth
import time
import json

url = "https://e621.net/posts.json?limit=320"
e621_agent = {
   'User-Agent': 'TagData (by USERNAME)', # replace with your username
   'login': 'EKrabs', # your username
   'api_key': '' # your api key
}

login = '' # your username
api_key = '' # your api key

max_id = 3011070 #3053317 3011070 2992268 518808
seen = {} #[]
run = 1
directory = 'C:/Scripts/Python/[adjective][species]/'
''' When refreshing data, change 'w' to 'a' '''
with open('{}JSON/e621-total-2021-11-05-a.json'.format(directory), 'w') as f:
	''' When refreshing data, replace f.write('[') to (',') '''
	f.write('[')
	while True:
		while_start = time.time()
		''' When refreshing data, change page=b{} to page=a{} '''
		r = requests.get('{}&page=b{}'.format(url, max_id), headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
		if r.status_code != 200:
			print(r.status_code)
			time.sleep(10)

		data = r.json()
		for item in data['posts']:
			post_id = item['id']
			md5 = item['file']['md5']
			''' Check if image was already indexed by comparing md5 '''
			if md5 in seen:
				continue
			seen[md5] = 1
			#seen.append(item['file']['md5'])
			print('#{} dumped {}'.format(run, post_id))
			f.write(json.dumps(item)) #+ '\n'
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
