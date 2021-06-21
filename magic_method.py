 #magic/special methods

class Book():


 	def __init__(self,sub,auth,pages):
 		self.sub=sub
 		self.auth=auth
 		self.pages=pages



 	#String representaion of the function.. always return
 	def __str__(self):
 		return 'This is the book of {} written by {} and contain {} pages'.format(self.sub,self.auth,self.pages)



 	def __len__(self):
 		return self.pages



my_book=Book('Python','Roy',4000)

print(my_book)

print str(my_book)
print len(my_book)

