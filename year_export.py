import requests
from requests.auth import HTTPBasicAuth
import time
import json

directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}e621-total-2021-10-25-a.json'.format(directory), 'r') as f:
    data = json.load(f)

with open('{}year-out.json'.format(directory), 'w') as o:
    o.write('[')
    run = 0
    for item in data:
        year = item['upload-date']
        o.write(json.dumps(year))
        o.write(',')
        print('Item #{}, Years Dumped'.format(run))
        run += 1
    o.write(']')
