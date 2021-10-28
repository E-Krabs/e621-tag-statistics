import json
import collections
import pandas as pd
import matplotlib.pyplot as plt

directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}date-out.json'.format(directory)) as f:
	data = f.read().split(',')

	yearcount = {}
	years = []
	posts = []
	for item in data:
		year = item.split('-')[0][1:]
		if year not in yearcount:
			yearcount[year] = 1
		else:
			yearcount[year] += 1
	word_counter = collections.Counter(yearcount)
	with open('{}year_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		#for year, count in word_counter.most_common():
		for year, count in word_counter:
			print(year, count)
			year_min =
			year_max = 
			
			#o.write('{0}: {1}\n'.format(year, count))
			#years.append(year)
			#posts.append(count)

	plt.plot(years, posts, color='red', label='Count')
	plt.title('Posted Per Year ({0}, ' - ', {1})'.format(year_min, year_max)
	plt.xlabel('Year')
	plt.ylabel('Posts')
	plt.grid()
	plt.legend()
	plt.show()
