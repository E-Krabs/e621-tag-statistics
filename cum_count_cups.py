import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
plt.style.use(['dark_background'])

tag1 = 'cum'
omit_final = True
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
		print('{}: {}-{}'.format(key, tag1, r1))
		tr = (key, r1) #tupled result
		lst.append(tr)

	print('Plotting Cups of Cum...')
	df_min = pd.DataFrame(lst, columns = ['Date', '{}'.format(tag1)])
	if omit_final == True:
		df_min = df_min.iloc[1:, :]
	df_min['Date'] = pd.to_datetime(df_min['Date'])
	df_min = df_min.sort_values(by=['Date'], ascending=True)
	if omit_empty == True:
		dfe = df_min.loc[:, df_min.columns!='Date']
		df_min = df_min[(dfe != 0).all(1)]
	df_min['{}'.format(tag1)] = df_min['{}'.format(tag1)].multiply(.5) #every ejaculation is equal to ~half a teaspoon (US)
	df_min['{}'.format(tag1)] = df_min['{}'.format(tag1)].multiply(.020833333333295) #teaspoons (US) to cups (US)

	df_max = pd.DataFrame(lst, columns = ['Date', '{}'.format(tag1)])
	if omit_final == True:
		df_max = df_max.iloc[1:, :]
	df_max['Date'] = pd.to_datetime(df_max['Date'])
	df_max = df_max.sort_values(by=['Date'], ascending=True)
	if omit_empty == True:
		dfe = df_max.loc[:, df_max.columns!='Date']
		df_max = df_max[(dfe != 0).all(1)]
	df_max['{}'.format(tag1)] = df_max['{}'.format(tag1)].multiply(1) #every ejaculation is equal to ~half a teaspoon (US)
	df_max['{}'.format(tag1)] = df_max['{}'.format(tag1)].multiply(.020833333333295) #teaspoons (US) to cups (US)

	plt.plot(df_min['Date'], df_min['{}'.format(tag1)], color='r', label='{} 1/2 TSP'.format(tag1))
	plt.plot(df_max['Date'], df_max['{}'.format(tag1)], color='b', label='{} 1 TSP'.format(tag1))
	plt.fill_between(df_max['Date'], df_min['{}'.format(tag1)], df_max['{}'.format(tag1)], color='c')
	#plt.title('Cum Counter TM')
	plt.ylabel('Cups (US) of Cum')
	plt.xticks(rotation=60)
	plt.legend()
	plt.savefig('{}cum_counter_cups_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True
