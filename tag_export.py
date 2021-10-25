directory = 'C:/'
with open('{}e621-total-m10-d24-y21.json'.format(directory), 'r') as f:
    r = f.read()

data = json.loads(r)
with open('{}tag-out.json'.format(directory), 'w') as o:
    o.write('[')
    runs = 0
    for item in data['posts']:
        tags = item['tags']
        o.write(json.dumps(tags, indent=2))
        o.write(',')
        print('#{}, dumped {1}'.format())
        runs += 1
    o.write(']')
    
