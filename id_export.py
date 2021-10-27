import requests
from requests.auth import HTTPBasicAuth
import time
import json

directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}e621-total-2021-10-25-a.json'.format(directory), 'r') as f:
    data = json.load(f)

with open('{}id-out.json'.format(directory), 'w') as o:
    o.write('[')
    run = 1
    for item in data:
        ids = item['id']
        o.write(json.dumps(ids))
        o.write(',')
        print('Item #{}, Ids Dumped'.format(run))
        run += 1
    o.write(']')