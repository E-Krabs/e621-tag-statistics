import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from itertools import cycle
import seaborn as sns
plt.style.use(['dark_background'])
colors = cycle(['blue', 'aqua', 'yellow', 'purple', 'pink', 'brown', 'grey', 'red', 'green', 'orange', 'white'])

omit_final = True
omit_empty = False
tag_total = []
tag_count = 0
print('Separate by ENTER')
while True:
	tag_count += 1
	item = input('Enter Tag {}: '.format(tag_count))
	if item == '':
		break
	tag_total.append(item)
#tag_total = ['fox', 'human', 'dragon', 'domestic_dog', 'wolf', 'horse', 'domestic_cat', 'rabbit', 'bird', 'tiger', 'fish', 'lion', 'lizard', 'snake']
#tag_total = ['canid', 'cetacean', 'felid', 'lagomorph', 'marsupial', 'mustelid', 'primate', 'rodent', 'skunk', 'rabbit', 'viverrid']
#skunk and rabbit are on their own, bc they do not belong to a family on e621.
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

		species = key['tags']['species']
		for word in species:
			if word not in dic['{}'.format(created_at)]:
				dic['{}'.format(created_at)][word] = 1
			else:
				dic['{}'.format(created_at)][word] += 1

	lst = []
	for key in dic:
		run = 0
		d = {}
		for tag in tag_total:
			run += 1
			try:
				d['r'+str(run)] = dic[key]['{}'.format(tag)] #result 1
			except:
				d['r'+str(run)] = 0
		tr = [key]
		for i in range(len(tag_total)):
			tr.append(d['r'+str(i+1)])
		lst.append(tr)

	print('Plotting...')
	column_lst = ['Date']
	for i in range(len(tag_total)):
		column_lst.append(tag_total[i])
	df = pd.DataFrame(lst, columns=column_lst)
	if omit_final == True:
		df = df.iloc[1:, :]
	df['Date'] = pd.to_datetime(df['Date'])
	df = df.sort_values(by=['Date'], ascending=True)
	if omit_empty == True:
		dfe = df.loc[:, df.columns!='Date']
		df = df[(dfe != 0).all(1)]

	for tag in tag_total:
		plt.plot(df['Date'], df['{}'.format(tag)], color=next(colors), linewidth='.5', label='{}'.format(tag))
	#plt.title('Tag Count Comparison')
	plt.xticks(rotation=60)
	if len(tag_total) >= 10:
		plt.legend(bbox_to_anchor=(1.04,1), borderaxespad=0)
	else:
		plt.legend()
	save_str = ''
	for tag in tag_total:
		save_str = save_str + tag + '_'
	plt.savefig('{}{}plot.png'.format(directory, save_str), dpi=300, bbox_inches='tight') #transparent=True
