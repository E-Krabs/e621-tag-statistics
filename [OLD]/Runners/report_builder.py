from bs4 import BeautifulSoup, Tag
# load the file
img_loc = input('Name of Image: ')
num = input('Report Number: ')
name = input('Title: ')
desc = input('Description: ')

with open("c:/Scripts/Python/[adjective][species]/template.htm") as f:
	contents = f.read()
	soup = BeautifulSoup(contents, 'lxml')

	soup.title.append('{}'.format(num))	
	soup.code.append('{}'.format(desc))
	soup.center.h2.append('{}'.format(name))
	image = soup.new_tag('img', src='/e621-json-dump/Report/{}.png'.format(img_loc), style='max-height:65%; max-width:65%;')
	#soup.center.append(name)
	soup.center.div.append(image)

# save the file again
with open("existing_file.html", "w") as outf:
	outf.write(str(soup))