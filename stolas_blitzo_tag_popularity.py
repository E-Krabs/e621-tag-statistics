import json
import json
import collections
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use(['dark_background'])

tag1 = 'stolas_(helluva_boss)'
tag2 = 'blitzo_(helluva_boss)'
display = 20
print('Loading JSON...')
directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}JSON/tag-out.json'.format(directory), 'r') as f:
	data = json.load(f)

	print('Counting...')
	dic = {}
	for key in data:
		general = key['tag']['general']
		character = key['tag']['character']
		if tag1 in character and tag2 in character:
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
	#plt.title('Stolas & Blitzo\'s Popular Tags')
	#plt.show()
	plt.savefig('{}{}_{}_popular_tags.png'.format(directory, tag1, tag2), dpi=300, bbox_inches='tight') #transparent=True
	#penis penis penis penis pp enlargement pills cum in ur mum\'s bum
	
	'''
	for key in data:
		characters = []
		general = key['tags']['general']
		character = key['tags']['character']
		for item in character: #add the charcters to a list and append list to a list, then count how many times tag1 and tag2 appear in the same list.
			characters.append(item)
			lst.append(characters)

	dic = {}
	for item in lst:
		if tag1 in item and tag2 in item: #if stolas and blitzo in list
				for key in data:
	'''
