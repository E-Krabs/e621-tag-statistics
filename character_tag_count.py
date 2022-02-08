import sqlite3
import json
import collections
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from datetime import datetime

plt.style.use(['dark_background'])
directory = 'C:/Scripts/Python/e621-json-dump-main'
print('connecting to database')
db = sqlite3.connect('{}/JSON/jsql.sqlite'.format(directory))
cursor = db.cursor()
fetch_query = "SELECT tags FROM myTable"
cursor.execute(fetch_query)
data = cursor.fetchall()
data = set(data)

def character_tag_counter(tag_name):
	print(tag_name)
	dic = {}
	for row in tqdm(data):
		tags = json.loads(row[0])
		general = tags['general']
		character = tags['character']
		for tag in character:
			if tag == tag_name:
				for tag in general:
					if tag not in dic:
						dic[tag] = 1
					else:
						dic[tag] += 1

	tag_count = collections.Counter(dic)
	with open('{}{}_popular_tags.txt'.format(directory, tag_name), 'w', encoding='utf-8') as o:
		for tag, count in tag_count.most_common():
			o.write('{}: {}\n'.format(tag, count))

	lst = tag_count.most_common(20)
	df = pd.DataFrame(lst, columns = [tag_name, 'Count'])
	df.plot.bar(x=tag_name,y='Count')
	plt.savefig('{}/{}_tag_plot.png'.format(directory, tag_name), dpi=300, bbox_inches='tight') #transparent=True
	plt.close() #clear plot vars

character_tag_counter('loona_(helluva_boss)')