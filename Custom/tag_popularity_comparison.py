import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
plt.style.use(['dark_background'])

tag1 = input('First Tag to Compare: ')
tag2 = input('Second Tag to Compare: ')
omit_f = input('Omit Final? (y, n):')
omit_e = input('Omit empty? (y, n):')
if omit_f == 'y':
	omit_final = True
else:
	omit_final = False
if omit_e == 'y':
	omit_empty = True
else:
	omit_empty = False
print('Loading JSON...')
directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}JSON/tag-out.json'.format(directory), 'r') as f:
	data = json.load(f)

	print('Counting...')
	dic = {}
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
		print('{}: {}-{}, {}-{}'.format(key, tag1, r1, tag2, r2))
		tr = (key, r1, r2) #tupled result
		lst.append(tr)
		
	print('Plotting...')
	df = pd.DataFrame(lst, columns = ['Date', '{}'.format(tag1), '{}'.format(tag2)])
	if omit_final == True:
		df = df.iloc[1:, :]
	df['Date'] = pd.to_datetime(df['Date'])
	df = df.sort_values(by=['Date'], ascending=True)
	if omit_empty == True:
		dfe = df.loc[:, df.columns!='Date']
		df = df[(dfe != 0).all(1)]
	plt.plot(df['Date'], df['{}'.format(tag1)], color='g', label='{}'.format(tag1))
	plt.plot(df['Date'], df['{}'.format(tag2)], color='r', label='{}'.format(tag2))
	plt.title('Popularity of {} & {}'.format(tag1, tag2))
	plt.xticks(rotation=60)
	plt.legend()
	plt.savefig('{}{}_{}_plot.png'.format(directory, tag1, tag2), dpi=300, bbox_inches='tight') #transparent=True
