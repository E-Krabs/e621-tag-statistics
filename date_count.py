import json
import collections
import pandas as pd
import matplotlib.pyplot as plt

directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}date-out.json'.format(directory)) as f:
	data = f.read().split(',')

	yearcount = {}
	for item in data:
		year = item.split('-')[0][1:]
		if year not in yearcount:
			yearcount[year] = 1
		else:
			yearcount[year] += 1
	word_counter = collections.Counter(yearcount)
	with open('{}posts_per_year_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		for year, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(year, count))

	print('Plotting Posts Per Year...')
	lst = word_counter.most_common(5)
	df = pd.DataFrame(lst, columns = ['Year', 'Posts'])
	df = df.sort_values(by=['Year'], ascending=True)
	df.plot(x='Year', y='Posts', color='red')
	plt.title('Posted Per Year (2008-2021)')
	plt.savefig('{}posts_per_year_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True

	print('Plotting Total Posts...')
	lst = word_counter.most_common(5)
	df = pd.DataFrame(lst, columns = ['Year', 'Posts'])
	df = df.sort_values(by=['Year'], ascending=True)
	
	df.plot(x='Year', y='Posts', color='red')
	plt.title('Posted Per Year (2008-2021)')
	plt.savefig('{}posts_per_year_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True

