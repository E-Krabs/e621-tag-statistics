import json
import json
import collections
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use(['dark_background'])

pool_id = 23200
display = 20
print('Loading JSON...')
directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}JSON/tag-out-p.json'.format(directory), 'r') as f:
	data = json.load(f)

	print('Counting...')
	dic = {}
	for key in data:
		general = key['tags']['general']
		pools = key['pools']
		for item in pools:
			print(item)
			print(pool_id)
			if int(item) == pool_id:
				for word in general:
					if word not in dic:
						dic[word] = 1
					else:
						dic[word] += 1

	word_counter = collections.Counter(dic)
	with open('{}pool_{}_tag_count.txt'.format(directory, pool_id), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))
		
	print('Plotting...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['Tag', 'Count'])
	df.plot.bar(x='Tag',y='Count')
	#plt.title('Pool {}\'s Tags (20)')
	#plt.show()
	plt.savefig('{}pool_{}_tag_plot.png'.format(directory, pool_id), dpi=300, bbox_inches='tight') #transparent=True
