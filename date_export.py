import json

print('Loading JSON...')
directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}e621-total-2021-10-25-a.json'.format(directory), 'r') as f:
    data = json.load(f)

print('Exporting...')
with open('{}date-out.json'.format(directory), 'w') as o:
    o.write('[')
    run = 0
    for item in data:
        date = item['created_at']
        o.write(json.dumps(date))
        o.write(',')
        #print('Item #{}, Dates Dumped'.format(run))
        run += 1
    o.write(']')