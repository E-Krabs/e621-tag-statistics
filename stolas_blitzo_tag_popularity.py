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
	lst = []
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
