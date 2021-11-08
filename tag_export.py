import requests
from requests.auth import HTTPBasicAuth
import time
import json

directory = 'C:/Scripts/Python/[adjective][species]/'
print("Loading JSON...")
with open('{}JSON/e621-total-2021-11-05-a.json'.format(directory), 'rb') as f:
	data = json.load(f)

with open('{}JSON/tag-out.json'.format(directory), 'w') as o:
	o.write('[')

	print('Exporting...')
	dic = {}
	for key in data:
		y = key['created_at'].split('-')[0]
		m = key['created_at'].split('-')[1]
		created_at = '{}-{}'.format(y, m)
		size = key['file']['size']
		rating = key['rating']
		tags = key['tags']
		dic['created_at'] = created_at
		dic['size'] = size
		dic['rating'] = rating
		dic['tags'] = tags
		o.write(json.dumps(dic))
		o.write(',')
	o.write(']')
