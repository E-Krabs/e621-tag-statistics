import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime

omit_final = True
omit_empty = False
tag1 = 'vaginal'
tag2 = 'anal'
tag3 = 'oral'
tag4 = 'fellatio'
tag5 = 'fingering'
tag6 = 'handjob'
tag7 = 'cunnilingus'
print('Loading JSON...')
directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}JSON/tag-out.json'.format(directory), 'rb') as f:
	data = json.load(f)

	print('Counting...')
	dic = {}
	#run = 0
	for key in data:
		y = key['created_at'].split('-')[0]
		m = key['created_at'].split('-')[1]
		created_at = '{}-{}'.format(y, m)

		if created_at not in dic:
			dic[created_at] = {}
		general = key['tags']['general']

		for word in general:
			if word not in dic['{}'.format(created_at)]:
				dic['{}'.format(created_at)][word] = 1
			else:
				dic['{}'.format(created_at)][word] += 1
		#run += 1
		#print(run)

	print('Listing...')
	#with open('{}'.format(directory), 'w') as o:
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
		try:
			r6 = dic[key]['{}'.format(tag5)] #result 4
		except:
			r6 = 0
		try:
			r7 = dic[key]['{}'.format(tag5)] #result 4
		except:
			r7 = 0
		print('{}: {}-{}, {}-{}, {}-{}, {}-{}, {}-{}, {}-{}, {}-{}'.format(key, tag1, r1, tag2, r2, tag3, r3, tag4, r4, tag5, r5, tag6, r6, tag7, r7))
		tr = (key, r1, r2, r3, r4, r5, r6, r7) #tupled result
		lst.append(tr)
		
	print('Plotting Popularity...')
	df = pd.DataFrame(lst, columns = ['Date', '{}'.format(tag1), '{}'.format(tag2), '{}'.format(tag3), '{}'.format(tag4), '{}'.format(tag5), '{}'.format(tag6), '{}'.format(tag7)])
	if omit_final == True:
		df = df.iloc[1:, :]
	df['Date'] = pd.to_datetime(df['Date'])
	df = df.sort_values(by=['Date'], ascending=True)
	if omit_empty == True:
		dfe = df.loc[:, df.columns!='Date']
		df = df[(dfe != 0).all(1)]
	plt.plot(df['Date'], df['{}'.format(tag1)], color='g', label='{}'.format(tag1))
	plt.plot(df['Date'], df['{}'.format(tag2)], color='r', label='{}'.format(tag2))
	plt.plot(df['Date'], df['{}'.format(tag3)], color='b', label='{}'.format(tag3))
	plt.plot(df['Date'], df['{}'.format(tag4)], color='m', label='{}'.format(tag4))
	plt.plot(df['Date'], df['{}'.format(tag5)], color='y', label='{}'.format(tag5))
	plt.plot(df['Date'], df['{}'.format(tag6)], color='c', label='{}'.format(tag6))
	plt.plot(df['Date'], df['{}'.format(tag7)], color='k', label='{}'.format(tag7))
	#plt.title('Relative Popularity of Basic Sex Acts')
	plt.xticks(rotation=60)
	plt.legend()
	plt.savefig('{}{}_{}_{}_{}_{}_{}_{}_plot.png'.format(directory, tag1, tag2, tag3, tag4, tag5, tag6, tag7), dpi=300, bbox_inches='tight') #transparent=True
	