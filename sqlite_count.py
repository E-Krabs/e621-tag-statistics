import sqlite3
import ast
import collections
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use(['dark_background'])

directory = 'C:/Scripts/Python/e621-json-dump-main'
db = sqlite3.connect('{}/JSON/jsql.sqlite'.format(directory))
cursor = db.cursor()
fetch_query = "SELECT tags FROM myTable"
cursor.execute(fetch_query)
data = cursor.fetchall()

def tag_counter(tag_type):
	print(tag_type)
	tags = {}
	for row in data:
		for key in row:
			key = ast.literal_eval(key)
			general = key[tag_type]
			#print(general)
			for tag in general:
				if tag not in tags:
					tags[tag] = 1
				else:
					tags[tag] += 1

	tag_count = collections.Counter(tags)
	with open('{}/{}_tag_count.txt'.format(directory, tag_type), 'w', encoding='utf-8') as o:
		for tag, count in tag_count.most_common():
			o.write('{}: {} \n'.format(tag, count))

	lst = tag_count.most_common(20)
	df = pd.DataFrame(lst, columns=[tag_type, 'Count'])
	df.plot.bar(x=tag_type, y='Count')
	plt.ticklabel_format(axis='y', style='plain')
	plt.savefig('{}/{}_tag_plot.png'.format(directory, tag_type), dpi=300, bbox_inches='tight')

tag_counter('general')
tag_counter('species')
tag_counter('character')
tag_counter('artist')
print(len(data))
