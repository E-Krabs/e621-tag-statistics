import os
import sqlite3
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from tqdm import tqdm
from itertools import cycle
from datetime import datetime

plt.style.use(['dark_background'])
colors = cycle(['blue', 'aqua', 'yellow', 'red', 'pink', 'brown', 'grey', 'purple', 'green', 'orange', 'white'])
omit_final = True
omit_empty = False
cwd = os.getcwd()
print('connecting to database')
db = sqlite3.connect('{}/JSON/jsql.sqlite'.format(cwd))
cursor = db.cursor()
fetch_query = "SELECT created_at, tags FROM myTable"
cursor.execute(fetch_query)
data = cursor.fetchall()
data = set(data)

def initalize_tag_count(tag_type): #adds a type of tag to memory as dict for counting
	print(tag_type)
	dic = {}
	for row in tqdm(data): #for every row in data as tuple of created_at and tags from sqlite fetch
		created_at = row[0]
		tags = json.loads(row[1])
		year = created_at.split('-')[0].replace('"', '')
		month = created_at.split('-')[1]
		created_at = '{}-{}'.format(year, month)
		if created_at not in dic:
			dic[created_at] = {}
		general = tags[tag_type]
		for tag in general:
			if tag not in dic['{}'.format(created_at)]:
				dic['{}'.format(created_at)][tag] = 1
			else:
				dic['{}'.format(created_at)][tag] += 1
	return(dic)

def tag_count_per_month(*tag_name): #i wrote this months ago, i forgot how it works
	print(tag_name)
	lst = []
	for key in tqdm(dic):
		run = 0
		d = {}
		for tag in tag_name:
			run += 1
			try:
				d['r'+str(run)] = dic[key]['{}'.format(tag)]
			except:
				d['r'+str(run)] = 0
		tr = [key]
		for i in range(len(tag_name)):
			tr.append(d['r'+str(i+1)])
		lst.append(tr)

	column_lst = ['Date']
	for i in range(len(tag_name)):
		column_lst.append(tag_name[i])
	df = pd.DataFrame(lst, columns=column_lst)
	if omit_final:
		df = df.iloc[1:, :]
	df['Date'] = pd.to_datetime(df['Date'])
	df = df.sort_values(by=['Date'], ascending=True)
	if omit_empty:
		dfe = df.loc[:, df.columns!='Date']
		df = df[(dfe != 0).all(1)]

	for tag in tag_name:
		if len(tag_name) > 6:
			plt.plot(df['Date'], df['{}'.format(tag)], color=next(colors), linewidth='.5', label='{}'.format(tag))
		else:
			plt.plot(df['Date'], df['{}'.format(tag)], color=next(colors), linewidth='1', label='{}'.format(tag))
	#plt.title('Tag Count Comparison')
	plt.xticks(rotation=60)
	if len(tag_name) >= 13:
		plt.legend(bbox_to_anchor=(1.04,1), borderaxespad=0)
	else:
		plt.legend()
	save_str = ''
	for tag in tag_name:
		save_str = save_str + tag + '_'
	plt.savefig('{}/{}plot.png'.format(cwd, save_str), dpi=300, bbox_inches='tight') #transparent=True
	plt.close() #clear plot vars

dic = initalize_tag_count('general')
tag_count_per_month('girly','tomboy','crossdressing', 'thigh_highs')
#girly - feminine male
#tomboy - masculine female
#crossdressing - opposite gender clothing
#thigh_highs - see relationship between femboys and thigh high socks
'''
dic = initalize_tag_count('species') #count all in species
tag_count_per_month('canid', 'cetacean', 'felid', 'equid', 'cervid', 'lagomorph', 'marsupial', 'mustelid', 'primate', 'rodent', 'skunk', 'viverrid')
tag_count_per_month('fox', 'human', 'dragon', 'domestic_dog', 'wolf', 'horse', 'domestic_cat', 'rabbit', 'bird', 'tiger', 'fish', 'lion', 'lizard', 'snake')
'''
