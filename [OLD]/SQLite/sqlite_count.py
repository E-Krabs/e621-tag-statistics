import os
import sqlite3
import json
import collections
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from datetime import datetime
from fnmatch import fnmatch

plt.style.use(['dark_background'])
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
fetch_query = 'SELECT file, tags, rating FROM e621'
cursor.execute(fetch_query)
data = cursor.fetchall()
data = set(data)

def tag_counter(tag_type):
	print(tag_type)
	dic = {}
	for row in tqdm(data): #for every row in data as tuple of rating, file, tags from sqlite fetch
		tags = json.loads(row[1]) #load second obj in tuple as json (tags)
		general = tags[tag_type]
		for tag in general:
			if tag not in dic:
				dic[tag] = 1
			else:
				dic[tag] += 1

	tag_count = collections.Counter(dic)
	with open(f'{cwd}\\{tag_type}_tag_count.txt', 'w', encoding='utf-8') as o:
		for tag, count in tag_count.most_common():
			o.write(f'{tag}: {count}\n')

	lst = tag_count.most_common(20)
	df = pd.DataFrame(lst, columns=[tag_type, 'Count'])
	df.plot.bar(x=tag_type, y='Count')
	plt.ticklabel_format(axis='y', style='plain')
	plt.savefig(f'{cwd}\\{tag_type}_plot.png', dpi=300, bbox_inches='tight')
	plt.close() #clear plot vars

def rating_counter():
	print('rating')
	safe = 0
	questionable = 0
	explicit = 0
	x = []
	y = ['safe', 'questionable', 'explicit']
	for row in tqdm(data):
		rating = row[2] #load third obj in tuple (rating)
		for letter in rating:
			if letter == 's':
				safe += 1
			elif letter == 'q':
				questionable += 1
			elif letter == 'e':
				explicit += 1
	x.extend((safe, questionable, explicit))

	print('size')
	size_byte = 0
	for row in tqdm(data):
		file = json.loads(row[0]) #load second obj in tuple as json (file)
		size_byte += file['size']
	size_tb = size_byte // 1099511627776
	plt.barh(y, x)
	plt.title(f'Total Posts: {len(data)} (~{size_tb}TB)')
	plt.ticklabel_format(axis='x', style='plain')
	plt.savefig(f'{cwd}\\rating_plot.png', dpi=300, bbox_inches='tight') #transparent=True
	plt.close() #clear plot vars

def ingest_log():
	with open(f'{cwd}\\ingest_log.txt', 'w', encoding='utf-8') as o:
		o.write(str(datetime.now()))

tag_counter('general')
tag_counter('species')
tag_counter('character')
tag_counter('artist')
rating_counter()
ingest_log()
