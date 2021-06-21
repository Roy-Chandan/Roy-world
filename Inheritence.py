#Inheritence -- Call a class from another class

class Animal():

	def __init__(self):
		print ("Dog Class Created")


	def who_am_i(self):
		print ("I am an ANimal")



	def eat(self):
		print("I like to eat")


My_Animal = Animal()

My_Animal.eat()
My_Animal.who_am_i()



class Dog(Animal):

	def __init__(self):
		Animal.__init__(self)
		print ("Dog Created")


	def who_am_i(self):
		print ("I am a Dog")



My_Dog = Dog()
My_Dog.eat()
My_Dog.who_am_i()



