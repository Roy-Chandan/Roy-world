
class Account():


	def __init__(self,owner,balance=0):

		self.owner=owner
		self.balance=balance


	def deposit(self,dep_amt):

		self.balance = self.balance + dep_amt
		print ("Amount : {} has been deposited in your account".format(dep_amt))
		print ("New Balance : {}".format(self.balance))


	def withdraw(self,with_amt):

		if self.balance >= with_amt:
			self.balance = self.balance - with_amt
			print ("Amount : {} has been withdrawn from your account".format(with_amt))
			print ("New Balance : {}".format(self.balance))


		else:
			print ("Sorry, not enough funds. Available Balance : {}".format(self.balance))


	def __str__(self):
		return "Owner : {} \nBalance : {}".format(self.owner,self.balance)



My_account = Account('Roy',1000)
print (My_account)

My_account.deposit(500)

My_account.withdraw(300)