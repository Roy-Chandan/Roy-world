import os
import shutil
import datetime


path = '/home/roy/prac'

for folders,sub_folders,files in os.walk(path):

	print ('Currently in the folder: {}'.format(folders))
	print ('\n')

	print ('Subfoders are: ')
	for s in sub_folders:
		print ('\t {}'.format(sub_folders))

	print ('\n')

	print ('The files are :')
	for f in files:
		print ('\t {}'.format(files))


	print ('\n')




today=datetime.date.today()
print(today)
print (today.month)
print (today.ctime())