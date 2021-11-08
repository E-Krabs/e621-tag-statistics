import json
import json
import collections
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use(['dark_background'])

tag1 = 'stolas_(helluva_boss)'
display = 20
print('Loading JSON...')
directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}JSON/tag-out.json'.format(directory), 'r') as f:
	data = json.load(f)

	print('Counting...')
	dic = {}
	for key in data:
		general = key['tags']['general']
		character = key['tags']['character']
		for item in character:
			if item == tag1:
				for word in general:
					if word not in dic:
						dic[word] = 1
					else:
						dic[word] += 1

	word_counter = collections.Counter(dic)
	with open('{}{}_popular_tags.txt'.format(directory, tag1), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))
		
	print('Plotting...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['Tag', 'Count'])
	df.plot.bar(x='Tag',y='Count')
	#plt.title('Stolas\'s Popular Tags')
	#plt.show()
	plt.savefig('{}{}_popular_tags.png'.format(directory, tag1), dpi=300, bbox_inches='tight') #transparent=True
