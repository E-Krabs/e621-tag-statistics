import json
import pandas as pd

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
			dic[created_at] = {} #in dic, create empty dict with the name 2021-10
		general = key['tags']['general']

		for word in general:
			if word not in dic['{}'.format(created_at)]:
				dic['{}'.format(created_at)][word] = 1
			else:
				dic['{}'.format(created_at)][word] += 1

	for key in dic:
		r = dic[key]['anthro']
		print('{}: {}'.format(key, r))
		lst = dic(zip(key, r))
		
	print('Plotting Popularity...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['Date', 'Count'])
	df.plot.bar(x='Date',y='Count')
	plt.title('Characters (957,625)')
	#plt.show()
	plt.savefig('{}popularity_tag_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True
