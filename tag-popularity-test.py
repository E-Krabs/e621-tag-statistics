import json
import pandas as pd

print('Loading JSON...')
directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}e621-total-2021-10-25-a.json'.format(directory), 'r') as f:
	data = json.load(f)

	dic = {}
	for key in data:
		y = key['created_at'].split('-')[0]
		m = key['created_at'].split('-')[1]
		created_at = '{}-{}'.format(y, m)

		if created_at not in dic:
			dic[created_at] = {} #in dic, create empty dict with the name 2021-10
		general = key['tags']['general']

		for word in general:
			if word not in dic['{}'.format(created_at)]:
				dic['{}'.format(created_at)][word] = 1
			else:
				dic['{}'.format(created_at)][word] += 1

	#for key in dic.values():
	#	for key in key:
	#		print(key)
	for key in dic:
		r = dic[key]['anthro']
		print('{}: {}'.format(key, r))

	#temp = 'anthro'
	#res = [sub[temp] for sub in dic.values() if temp in sub.keys()]
  
	# printing result 
	#print("The extracted values : " + str(res)) 




	#with open('{}NIGGERNIGGER.txt'.format(directory), 'w', encoding='utf-8') as o:
		#o.write(str(dic))
