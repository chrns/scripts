import os

file_format = 'png'
input_dir  = './input/'
output_dir = './output/' + file_format + '/'

pdfCmd = 'inkscape ' + input_dir + '$filename$.svg -A --export-dpi=300 --export-area-drawing --export-pdf-version=1.5 --without-gui --export-pdf=' + output_dir + '$filename$.pdf'
pngCmd = 'inkscape ' + input_dir + '$filename$.svg -e --export-area-page --without-gui --export-dpi=150 --export-png=' + output_dir + '$filename$.png'
cmd = pdfCmd if (file_format is 'pdf') else pngCmd

files = []

for file in os.listdir(input_dir):
	if file.endswith('.svg'):
		files.append(file)
		#os.system(cmd.replace('$filename$', os.path.splitext(file)[0]))
		#print '\r[{0}] {1}%'.format('#'*(progress/10), progress)

print('Total number of files is ' + str(len(files)))

for progress, file in enumerate(files):
	os.system(cmd.replace('$filename$', os.path.splitext(file)[0]))
	complite = (100*(progress+1))/len(files)
	print('[{0}{1}] {2}%'.format('#'*(int(complite/4)), ' '*(int((100-complite)/4)), '{:3.2f}'.format(complite)), end='\r')

print('\ndone')