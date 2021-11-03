import json

directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}JSON/id-out.json'.format(directory)) as f:
	data = f.read().split(',')
	print('{} Posts'.format(len(data)))