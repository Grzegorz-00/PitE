from os import listdir
from os.path import isfile, join, isdir
import sys

def list_recurs(directory):

	dir_li = []
	file_li = []

	for f in listdir(directory):
		if isfile(join(directory,f)):
			file_li.append(f)
		if isdir(join(directory,f)):
			dir_li.append(f)
	dir_li.sort()
	file_li.sort()
 
	for s in dir_li:
 		print directory + '/' + s + '/' + '\033[92m' + '.' + '\033[0m'
 		temp = directory + '/' + s
 		list_recurs(temp)
 		#print temp
 	
	for s in file_li:
 		print directory + '/' + '\033[92m' + s + '\033[0m'
 		
if len(sys.argv) == 1:
	list_recurs("/")
if len(sys.argv) == 2:
	print '\033[92m' + "----File lister----" + '\033[0m'
	if sys.argv[1][-1] == '/':
		temp = sys.argv[1][:-1]
		list_recurs(temp)
	else:
		list_recurs(sys.argv[1])


