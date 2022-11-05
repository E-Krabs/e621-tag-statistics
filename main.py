import csv
# from collections import defaultdict
from itertools import cycle

import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm

csv.field_size_limit(922337203)

# tag_cats = defaultdict(set)
date_tags = {}
omit_final = True
omit_empty = False
colours = cycle(['blue', 'aqua', 'yellow', 'red', 'pink', 'brown', 'grey', 'purple', 'green', 'orange', 'white'])


'''
def tag_categorizer():
	with open('tags-2022-11-02.csv', encoding='utf8') as tag_cat_f:
		cat_reader = csv.reader(tag_cat_f, delimiter=',')
		cat_columns = next(cat_reader)

		for row in cat_reader:
			tag_name = row[1]
			tag_cat = row[2]
			tag_cats[f'{tag_cat}'].add(tag_name)
'''


def date_tag_frequency(interval):
	with open('shortened_csv.csv', encoding='utf8') as post_f:
		post_reader = csv.reader(post_f, delimiter=',')
		next(post_reader)

		for row in tqdm(post_reader, total=3900000):  # not the actual total, bc counting rows in post_reader is so slow
			created_at = row[2]
			y, m, d = created_at[:4], created_at[5:7], created_at[8:10]
			tags = row[8].split(' ')

			if interval == 'daily':
				created_at = f'{y}-{m}-{d}'
			elif interval == 'monthly':
				created_at = f'{y}-{m}'
			else:
				created_at = y

			if created_at not in date_tags:
				date_tags[created_at] = {}
			for tag in tags:
				if tag in tag_name:
					if tag not in date_tags[f'{created_at}']:
						date_tags[f'{created_at}'][tag] = 1
					else:
						date_tags[f'{created_at}'][tag] += 1


def date_tag_count():
	d = {}
	lst = []
	print(' '.join(tag_name))

	for date in date_tags:
		for tag in tag_name:
			try:
				d[f'{tag}'] = date_tags[date][f'{tag}']
			except:
				d[f'{tag}'] = 0

		tr = [date]
		for tag in tag_name:
			tr.append(d[f'{tag}'])
		lst.append(tr)

	column_lst = ['date']
	column_lst.extend(tag_name)

	df = pd.DataFrame(lst, columns=column_lst)
	if omit_final:
		df = df.iloc[1:, :]

	df['Date'] = pd.to_datetime(df.date)
	# df = df.sort_values(by=['Date'], ascending=True)
	if omit_empty:
		dfe = df.loc[:, df.columns != 'Date']
		df = df[(dfe != 0).all(1)]

	for tag in tag_name:
		if len(tag_name) > 6:
			plt.plot(df['Date'], df[f'{tag}'], color=next(colours), linewidth='.5', label=f'{tag}')
		else:
			plt.plot(df['Date'], df[f'{tag}'], color=next(colours), linewidth='1', label=f'{tag}')

	plt.title(', '.join(tag_name))
	plt.xticks(rotation=60)
	if len(tag_name) > 14:
		plt.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0)
	else:
		plt.legend()

	save_str = '_'.join(tag_name)
	plt.savefig(f'{save_str}_plot.png', dpi=300, bbox_inches='tight')
	plt.close()


tag_name = ['breasts', 'pussy', 'anthro']

date_tag_frequency('monthly')
date_tag_count()
