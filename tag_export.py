import requests
from requests.auth import HTTPBasicAuth
import time
import json

directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}e621-total-2021-10-25-a.json'.format(directory), 'r') as f:
    data = json.load(f)

with open('{}tag-out.json'.format(directory), 'w') as o:
    o.write('[')
    run = 0
    for item in data:
        tags = item['tags']
        o.write(json.dumps(tags))
        o.write(',')
        print('Item #{}, Tags Dumped'.format(run))
        run += 1
    o.write(']')