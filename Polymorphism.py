#Polymorphism

class Dog():

	def __init__(self,name):
		self.name=name


	def speak(self):
		return self.name + " says woof!"




class Cat():

	def __init__(self,name):
		self.name=name


	def speak(self):
		return self.name + " says meow!"



my_dog = Dog("Sammy")
my_cat = Cat("Kitty")


print(my_cat.speak())
print(my_dog.speak())



def pet_speak(pet):
	print (pet.speak())



pet_speak(my_dog)
pet_speak(my_cat)
