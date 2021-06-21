#collections module

from collections import Counter
mylist = [1,2,2,3,4,5,5,4,3,2,5,6,7,5]
Counter(mylist)



from collections import defaultdict


import os
os.getcwd()
os.listdir('C:\\Users')


import shutil
shutil.move('prac.txt','C:\\Users\\roych\\anaconda3')



path = 'C:\\Users\\roych\\anaconda3\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\Example_Top_Level'

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


##############################
#Datetime module

import datetime


today=datetime.date.today()
print(today)
print (today.month)
print (today.ctime())


####################
# math
import math





























