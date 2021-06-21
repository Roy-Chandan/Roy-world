
def even_check(num_list):

	Even_list = []

	for num in num_list:
		if num % 2 == 0:
			Even_list.append(num)

		else:
			pass


	return Even_list



lst = even_check([2,3,4,5,6])
print lst
