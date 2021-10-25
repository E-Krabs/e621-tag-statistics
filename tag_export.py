import requests
from requests.auth import HTTPBasicAuth
import time
import json

directory = 'C:/'
with open('{}e621-total-2021-10-25.json'.format(directory), 'r') as f:
    data = json.load(f)

with open('{}tag-out-2021-10-25.json'.format(directory), 'w') as o:
    o.write('[')
    run = 1
    for item in data:
        tags = item['tags']
        for tag in tags:
            o.write(json.dumps(tags, indent=2))
            o.write(',')
            print('Item #{}, Tags Dumped'.format(run))
            run += 1
    o.write(']')
    
