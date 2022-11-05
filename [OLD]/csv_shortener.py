import csv

csv.field_size_limit(922337203)

with open('posts-2022-11-01.csv', encoding='utf8') as long_csv, open('shortened_csv.csv', 'w', encoding='utf8') as short_csv:
	csv_reader = csv.reader(long_csv)
	csv_writer = csv.writer(short_csv, lineterminator='\n')

	for i, row in enumerate(csv_reader):
		if i <= 10000:
			print(i)
			csv_writer.writerow(row)
		else:
			exit()
