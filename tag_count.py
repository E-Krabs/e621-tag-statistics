import json
import collections
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use(['dark_background'])

display = 20 #int(input('Tags to Plot: '))
print('Loading JSON...')

directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}JSON/tag-out.json'.format(directory), 'r') as f:
	data = json.load(f)

	s = 0
	q = 0
	e = 0
	y = []
	x = ['safe', 'questionable', 'explicit']
	for key in data:
		rating = key['rating']
		for word in rating:
			if word == 's':
				s += 1
			elif word == 'q':
				q += 1
			elif word == 'e':
				e += 1
	y.append(s)
	y.append(q)
	y.append(e)
	plt.barh(y, x)

	dic = {}
	for key in data:
		general = key['tags']['general']
		for words in general:
			word = words
			if word not in dic:
				dic[word] = 1
			else:
				dic[word] += 1
	word_counter = collections.Counter(dic)
	with open('{}general_tag_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))

	print('Plotting General...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['General Tag', 'Count'])
	df.plot.bar(x='General Tag',y='Count')
	plt.ticklabel_format(axis='y', style='plain')
	#plt.title('General')
	#plt.show()
	plt.savefig('{}general_tag_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True

	dic = {}
	for key in data:
		species = key['tags']['species']
		for words in species:
			word = words
			if word not in dic:
				dic[word] = 1
			else:
				dic[word] += 1
	word_counter = collections.Counter(dic)
	with open('{}species_tag_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))

	print('Plotting Species...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['Species', 'Count'])
	df.plot.bar(x='Species',y='Count')
	plt.ticklabel_format(axis='y', style='plain')
	#plt.title('Species')
	#plt.show()
	plt.savefig('{}species_tag_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True

	dic = {}
	for key in data:
		character = key['tags']['character']
		for words in character:
			word = words
			if word not in dic:
				dic[word] = 1
			else:
				dic[word] += 1
	word_counter = collections.Counter(dic)
	with open('{}character_tag_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))

	print('Plotting Characters...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['Character', 'Count'])
	df.plot.bar(x='Character',y='Count')
	#plt.title('Characters')
	#plt.show()
	plt.savefig('{}character_tag_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True

	stopwords = ['conditional_dnp', 'unknown_artist']
	dic = {}
	for key in data:
		artist = key['tags']['artist']
		for words in artist:
			word = words
			if word not in stopwords:
				if word not in dic:
					dic[word] = 1
				else:
					dic[word] += 1
	word_counter = collections.Counter(dic)
	with open('{}artist_tag_count.txt'.format(directory), 'w', encoding='utf-8') as o:
		for word, count in word_counter.most_common():
			o.write('{0}: {1}\n'.format(word, count))

	print('Plotting Artists...')
	lst = word_counter.most_common(display)
	df = pd.DataFrame(lst, columns = ['Artist (Exc. conditional_dnp & unknown_artist)', 'Count'])
	df.plot.bar(x='Artist (Exc. conditional_dnp & unknown_artist)',y='Count')
	#plt.title('Artists')
	#plt.show()
	plt.savefig('{}artist_tag_plot.png'.format(directory), dpi=300, bbox_inches='tight') #transparent=True