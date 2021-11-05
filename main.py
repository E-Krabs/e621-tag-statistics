import requests
from requests.auth import HTTPBasicAuth
import time
import json

url = "https://e621.net/posts.json?limit=320"
e621_agent = {
   'User-Agent': '',
   'login': '',
   'api_key': ''
}

login = ''
api_key = ''

max_id = 3011070 #2992268
seen = []
run = 0
directory = 'C:/Scripts/Python/[adjective][species]/'
''' When refreshing data, change 'w' to 'a' '''
with open('{}e621-total-2021-11-05-a.json'.format(directory), 'w') as f:
	f.write('[')
	while max_id > 0:
		''' When refreshing data, change page=b{} to page=a{} '''
		r = requests.get('{}&page=b{}'.format(url, max_id), headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
		if r.status_code != 200:
			print('!!! 200 !!!')
		if r.status_code == 429:
			print('!!! 429 !!!')
		if r.status_code == 503:
			print('!!! 503 !!!')
		data = r.json()
		for item in data['posts']:
			post_id = item['id']
			if item['file']['md5'] in seen:
				continue
			seen.append(item['file']['md5'])
			#s.write(json.dumps(seen, indent=2))
			print('#{} dumped {}'.format(run, post_id))
			f.write(json.dumps(item))
			f.write(',')
		''' When refreshing data, change -= 320 to += 320 '''
		max_id -= 320
		time.sleep(2)
		run += 1
	f.write(']')

print('fetched {} records, with {} requests'.format(len(seen), run))
