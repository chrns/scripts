###
### This file help to build standalone book.md-file
###

from os import listdir
from os.path import isfile, join

path = './markdown/'
output_file = path + 'book.md'

files = [f for f in listdir(path) if isfile(join(path, f))]

with open(output_file, 'w', encoding='utf8') as out:
	for file in files:
		print('working with ' + file)
		with open(path + file, encoding='utf8') as f:
			for line in f:
				out.write(line)
		out.write('\n\n')


