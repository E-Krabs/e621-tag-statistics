import json
import collections
import pandas as pd
import matplotlib.pyplot as plt

display = 20 #int(input('Tags to Plot: '))
print('Loading JSON...')

directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}tag-out.json'.format(directory), 'r') as f:
	data = json.load(f)

	wordcount = {}
	for item in data:
		general = item['general']
		for words in general:
			word = words
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
	word_counter = collections.Counter(wordcount)
	with open('{}general_tag_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))

	print('Plotting General...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['General Tag', 'Count'])
	df.plot.bar(x='General Tag',y='Count')
	plt.title('General (957,625)')
	#plt.show()
	plt.savefig('{}general_tag_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True

	wordcount = {}
	for item in data:
		species = item['species']
		for words in species:
			word = words
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
	word_counter = collections.Counter(wordcount)
	with open('{}species_tag_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))

	print('Plotting Species...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['Species', 'Count'])
	df.plot.bar(x='Species',y='Count')
	plt.title('Species (957,625)')
	#plt.show()
	plt.savefig('{}species_tag_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True

	wordcount = {}
	for item in data:
		character = item['character']
		for words in character:
			word = words
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
	word_counter = collections.Counter(wordcount)
	with open('{}character_tag_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))

	print('Plotting Characters...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['Character', 'Count'])
	df.plot.bar(x='Character',y='Count')
	plt.title('Characters (957,625)')
	#plt.show()
	plt.savefig('{}character_tag_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True

	stopwords = ['conditional_dnp', 'unknown_artist']
	wordcount = {}
	for item in data:
		artist = item['artist']
		for words in artist:
			word = words
			if word not in stopwords:
				if word not in wordcount:
					wordcount[word] = 1
				else:
					wordcount[word] += 1
	word_counter = collections.Counter(wordcount)
	with open('{}artist_tag_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))

	print('Plotting Artists...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['Artist (Exc. conditional_dnp & unknown_artist)', 'Count'])
	df.plot.bar(x='Artist (Exc. conditional_dnp & unknown_artist)',y='Count')
	plt.title('Artists (957,625)')
	#plt.show()
	plt.savefig('{}artist_tag_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True
