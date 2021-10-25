import requests
from requests.auth import HTTPBasicAuth
import time
import json

url = "https://e621.net/posts.json?limit=1000"
e621_agent = {
   'User-Agent': 'TagData (by EKrabs)',
   'login': 'EKrabs',
   'api_key': '7yqTWqrn1CLk4nG6q4J1W6s4'
}

login = 'EKrabs'
api_key = '7yqTWqrn1CLk4nG6q4J1W6s4'

max_id = 2299865 #2990557
seen = []
directory = 'C:/Scripts/Python/[adjective][species]/'
run = 0
with open('{}e621-total-m10-d24-y21.json'.format(directory), 'a') as f:
    #with open('{}seen.json'.format(directory), 'w') as s:
    #s.write('[')
    f.write('[')
    while max_id > 0:
        r = requests.get('{0}&page=b{1}'.format(url, max_id), headers=e621_agent, auth=HTTPBasicAuth(login, api_key))
        if r.status_code != 200:
            print('Error got: {}'.format(r.status_code, r.text))
        if r.status_code == 429:
            print('!!! 429 !!!')
        data = r.json()
        for item in data['posts']:
            post_id = item['id']
            if item['file']['md5'] in seen:
                continue
            seen.append(item['file']['md5'])
            #s.write(json.dumps(seen, indent=2))
            print('#{0} Dumped {1}'.format(run, post_id))
            f.write(json.dumps(item, indent=2))
            f.write(',')
        max_id -= 1000
        time.sleep(2)
        run += 1
    f.write(']')
    #s.write(']')