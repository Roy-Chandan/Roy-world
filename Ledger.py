class Account ():



	def __init__(self,owner,amt=0):
		self.owner=owner
		self.amt=amt


	def deposit(self,dep_amt):
		self.amt = self.amt + dep_amt
		print 'Hello, Amount = {} has been added'.format(dep_amt)


	def withdraw(self,with_amt):

		if self.amt >= with_amt:
			self.amt = self.amt - with_amt
			print 'Hello, Amount : {} has been withdrawn'.format(with_amt)


		else:
			#amt < with_amt:
			print 'Sorry, you dont have enough funds'


	def __str__(self):
		retun "Owner : {} \n Balance : {}".format(self.owner,self.amt)