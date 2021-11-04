import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime

tag1 = 'nick_wilde'
tag2 = 'judy_hopps'
tag3 = 'fox'
tag4 = 'rabbit'
tag5 = 'zootopia'
print('Loading JSON...')
directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}JSON/e621-total-2021-10-25-a.json'.format(directory), 'r') as f:
	data = json.load(f)

	print('Counting...')
	dic = {}
	for key in data:
		y = key['created_at'].split('-')[0]
		m = key['created_at'].split('-')[1]
		created_at = '{}-{}'.format(y, m)

		if created_at not in dic:
			dic[created_at] = {}
		general = key['tags']['character']
		species = key['tags']['species']
		copyright = key['tags']['copyright']
		for word in general:
			if word not in dic['{}'.format(created_at)]:
				dic['{}'.format(created_at)][word] = 1
			else:
				dic['{}'.format(created_at)][word] += 1

		for word in species:
			if word not in dic['{}'.format(created_at)]:
				dic['{}'.format(created_at)][word] = 1
			else:
				dic['{}'.format(created_at)][word] += 1

		for word in copyright:
			if word not in dic['{}'.format(created_at)]:
				dic['{}'.format(created_at)][word] = 1
			else:
				dic['{}'.format(created_at)][word] += 1
				
	lst = []
	for key in dic:
		try:
			r1 = dic[key]['{}'.format(tag1)] #result 1
		except:
			r1 = 0
		try:
			r2 = dic[key]['{}'.format(tag2)] #result 2
		except:
			r2 = 0
		try:
			r3 = dic[key]['{}'.format(tag3)] #result 3
		except:
			r3 = 0
		try:
			r4 = dic[key]['{}'.format(tag4)] #result 4
		except:
			r4 = 0
		try:
			r5 = dic[key]['{}'.format(tag5)] #result 4
		except:
			r5 = 0
		print('{}: {}-{}, {}-{}'.format(key, tag1, r1, tag2, r2, tag3, r3, tag4, r4, tag5, r5))
		tr = (key, r1, r2, r3, r4, r5) #tupled result
		lst.append(tr)
		
	print('Plotting Popularity...')
	df = pd.DataFrame(lst, columns = ['Date', '{}'.format(tag1), '{}'.format(tag2), '{}'.format(tag3), '{}'.format(tag4), '{}'.format(tag5)])
	df['Date'] = pd.to_datetime(df['Date'])
	df = df.sort_values(by=['Date'], ascending=True)
	plt.plot(df['Date'], df['{}'.format(tag1)], color='g', label='{}'.format(tag1))
	plt.plot(df['Date'], df['{}'.format(tag2)], color='r', label='{}'.format(tag2))
	plt.plot(df['Date'], df['{}'.format(tag3)], color='b', label='{}'.format(tag3))
	plt.plot(df['Date'], df['{}'.format(tag4)], color='m', label='{}'.format(tag4))
	plt.plot(df['Date'], df['{}'.format(tag5)], color='k', label='{}'.format(tag5))
	plt.title('Zootopias Influence on Foxes and Rabbits')
	plt.xticks(rotation=60)
	plt.legend()
	plt.savefig('{}{}_{}_influence_plot.png'.format(directory, tag1, tag2), dpi=300, bbox_inches='tight') #transparent=True
