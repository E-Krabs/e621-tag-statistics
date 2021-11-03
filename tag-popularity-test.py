import json
import pandas as pd

tag1 = input('First Tag to Compare:')
tag2 = input('Second Tag to Compare:')

print('Loading JSON...')
directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}e621-total-2021-10-25-a.json'.format(directory), 'r') as f:
	data = json.load(f)

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
		r1 = dic[key]['{}'.format(tag1)]
		r2 = dic[key]['{}'.format(tag2)]
		print('{}: {}-{}, {}-{}'.format(key, tag1, r1, tag2, r2))
		lst.append(dic(zip(key, r1, r2)))
	print(lst)	
		
	#https://pythonguides.com/python-plot-multiple-lines/#Python_plot_multiple_lines_from_dataframe
		
	print('Plotting Popularity...')
	df = pd.DataFrame(lst, columns = ['Date', '{}'.format(tag1), '{}'.format(tag2)])
	df.plot(x='Date', y='{}'.format(tag1))
	df.plot(x='Date', y='{}'.format(tag2))
	plt.title('Popularity of {} & {}'.format(tag1, tag2))
	plt.show()
	#plt.savefig('{}{}_{}_plot.png'.format(directory, tag1, tag2), dpi=300, bbox_inches='tight') #transparent=True
