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

for fname in os.listdir('.'):
	if fname.endswith('.sqlite') == True:
		sqlite_file = cwd + '\\' + fname
		break
else:
	print('Please generate the database.')
	exit()

print(f'Connecting to {sqlite_file}')
db = sqlite3.connect(sqlite_file)
cursor = db.cursor()
fetch_query = 'SELECT created_at, tags FROM e621'
cursor.execute(fetch_query)
data = cursor.fetchall()
data = set(data)

def initalize_tag_count(tag_type): #adds tag to memory as a dic for counting
	print(tag_type)
	dic = {}
	for row in tqdm(data):
		created_at = row[0]
		tags = json.loads(row[1])
		year = created_at.split('-')[0].replace('"', '')
		month = created_at.split('-')[1]
		created_at = f'{year}-{month}'
		if created_at not in dic:
			dic[created_at] = {}
		general = tags[tag_type]
		for tag in general:
			if tag not in dic[f'{created_at}']:
				dic[f'{created_at}'][tag] = 1
			else:
				dic[f'{created_at}'][tag] += 1
	return(dic)

def tag_count_per_month(*tag_name):
	for tag in tag_name:
		print(tag_name)
	lst = []
	for key in tqdm(dic): #for every year in the dic of years
		run = 0
		d = {}
		for tag in tag_name: #for every tag in the tuple tag_name
			run += 1
			try:
				d['tag'+str(run)] = dic[key][f'{tag}'] #{'tag1': year_iteration's tag's number} = {'tag1': '315', 'tag2': '569'}
			except:
				d['tag'+str(run)] = 0
		tr = [key] #['2022-01']

		for i in range(len(tag_name)):
			tr.append(d['tag'+str(i+1)]) #['2022-01', '315', '569']
		lst.append(tr) #[['2022-01', '315', '569'], ...]

	column_lst = ['Date']
	for i in range(len(tag_name)):
		column_lst.append(tag_name[i])
	df = pd.DataFrame(lst, columns=column_lst) #  Date | tag1 | tag2
	if omit_final:                             # 2022-01  315   569
		df = df.iloc[1:, :]
	df['Date'] = pd.to_datetime(df['Date'])
	df = df.sort_values(by=['Date'], ascending=True)
	if omit_empty:
		dfe = df.loc[:, df.columns!='Date'] #locate rows not in date
		df = df[(dfe != 0).all(1)] #dataframe = all rows that are equal to 1?

	for tag in tag_name:
		if len(tag_name) > 6:
			plt.plot(df['Date'], df[f'{tag}'], color=next(colors), linewidth='.5', label=f'{tag}')
		else:
			plt.plot(df['Date'], df[f'{tag}'], color=next(colors), linewidth='1', label=f'{tag}')
	#plt.title('Tag Count Comparison')
	plt.xticks(rotation=60)
	if len(tag_name) >= 13:
		plt.legend(bbox_to_anchor=(1.04,1), borderaxespad=0)
	else:
		plt.legend()
	
	save_str = ''
	for tag in tag_name:
		if '/' in tag:
			tag = tag.replace('/', '-')
		elif '\\' in tag:
			tag = tag.replace('\\', '-')
		save_str = save_str + tag + '_'

	plt.savefig(f'{cwd}\\{save_str}plot.png', dpi=300, bbox_inches='tight') #transparent=True
	plt.close() #clear plot vars

####GENERAL EXAMPLE
dic = initalize_tag_count('general')
#tag_count_per_month('intersex/male', 'intersex/female', 'gynomorph')
#tag_count_per_month('girly','tomboy','crossdressing', 'thigh_highs')
tag_count_per_month('female', 'male')
####CHARACTER EXAMPLE
#dic = initalize_tag_count('character')
#tag_count_per_month('nicole_watterson', 'gumball_watterson', 'richard_watterson')

####SPECIES EXAMPLE
#dic = initalize_tag_count('species') #count all in species
#tag_count_per_month('canid', 'cetacean', 'felid', 'equid', 'cervid', 'lagomorph', 'marsupial', 'mustelid', 'primate', 'rodent', 'skunk', 'viverrid')
#tag_count_per_month('fox', 'human', 'dragon', 'domestic_dog', 'wolf', 'horse', 'domestic_cat', 'rabbit', 'bird', 'tiger', 'fish', 'lion', 'lizard', 'snake')
