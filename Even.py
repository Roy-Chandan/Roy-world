def even_check(num_list):
	for num in num_list:
		if num % 2 == 0:
			return True
		else:
			pass

	return False


	#return num % 	2 == 0
	
res = even_check ([1,3,5])
print res