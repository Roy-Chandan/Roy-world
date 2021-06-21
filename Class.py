
class Dog():


	#Class Object Attribute
	#Same for any instance of the Class

	species = 'mammal'

	def __init__(self,breed,name,spots):

	# init works as a constructor for a class
	# self is the instance of the object itself
	# breed is the argument

		self.breed=breed
		self.name=name
		self.spots=spots


	# Operations/Actions --> Methods
	# Method is a function that is inside a class
	def bark(self,food):
		print('Woof! My Name is {} and I like {} and I am a {}'.format(self.name,food,Dog.species))




#my_dog=Dog(breed='Lab',name='Sam',spots=True)
my_dog=Dog('Lab','Sam','False')


res = my_dog.breed
res1=my_dog.species

print res
print res1


my_dog.bark('Bone')


