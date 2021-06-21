
def user_input() :

	accept_range = range(0,100)
	
	within_range = False
	int_num = 'Wrong'


	while int_num.isdigit()==False or within_range==False:

		int_num = input ("Enter a  number between 1 to 10:")


		if int_num.isdigit==False:
			print ("Please enter a digit, not string")
			


		if int_num.isdigit()==True:

			if int_num in accept_range():
				within_range = True


			else:
				print ("Please enter a number between 1-100")
				within_range= False



	return int(int_num)




result=user_input()
print result