import os
import csv
import requests
import shutil

from tqdm import tqdm

csv.field_size_limit(922337203)
cwd = os.getcwd()
dld = 'F:\\path\\to\\dl'

def downloader():
	tag_dir = '_'.join(include_tags)
	os.makedirs(f'{dld}\\{tag_dir}', exist_ok=True)

	with open(f'{cwd}\\posts-2022-12-19.csv', encoding='utf8') as post_f:
		post_reader = csv.reader(post_f, delimiter=',')
		next(post_reader)

		for row in tqdm(post_reader, total=3800000):  # estimation
			tags = row[8].split(' ')

			if all(tag in tags for tag in include_tags) and (tag not in exclude_tags for tag in tags):
				md5, file_ext = row[3], row[11]
				r = requests.get(f'https://static1.e621.net/data/{md5[:2]}/{md5[2:4]}/{md5}.{file_ext}', stream=True)

					if r.status_code == 200:
						with open(f'{dld}\\{tag_dir}\\{md5}.{file_ext}', 'wb') as f:
							r.raw.decode_content = True
							shutil.copyfileobj(r.raw, f)

			'''
			for tag in tags:
				if tag == tag_name and tag not in exclude_tags:
					md5, file_ext = row[3], row[11]

					r = requests.get(f'https://static1.e621.net/data/{md5[:2]}/{md5[2:4]}/{md5}.{file_ext}', stream=True)
					if r.status_code == 200:
						with open(f'{dld}\\{tag_name}\\{md5}.{file_ext}', 'wb') as f:
							r.raw.decode_content = True
							shutil.copyfileobj(r.raw, f)
			'''

# can be a single tag, but must be in list
include_tags = ['fur', 'anthro']
exclude_tags = ['', '']

downloader()
