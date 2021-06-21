# args and kwargs
# *args returns tuple and **kwargs returns dictionary

def my_arg(*args):
	return sum(args) * .5


res = my_arg(10,20,30,40)



def my_kwarg(**kwargs):
	if 'fruit' in kwargs:
		print ('My fav fruit is {}'.format(kwargs['fruit']))
	else:
		print ('I didnt find my fruit here')


res1 = my_kwarg(fruit='mango',veg='lettuce')





def my_func(*args,**kwargs):

	print (args)
	print (kwargs)

	print ('I have {} {}'.format(args[0],kwargs['fruit']))



res3 = my_func (10,20,30,fruit='mango',veg='lett')





print res
print res1
print res3