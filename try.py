
def user_input():

	try:

		res = int(input("Please provide a number: "))

	except:
		print ("This is not an integer!")


	finally:
		print("End of try/except/finally")



#user_input()




def input_user():

	while True:

		try:

			res = int(input("Please Provide a number :"))

		except:
			print ("This is not a number")
			continue


		else:
			print ("number accepted")
			break


input_user()