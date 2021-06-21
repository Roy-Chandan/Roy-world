
work_hours = [('Sona',100),('Roy',900),('Riya',200)]


def emp_of_month(work_hours):

	max = 0
	emp = ''


	for name,hours in work_hours:
		if hours > max:
			emp = name
			max = hours

		else:
			pass


	return (emp,max)


result = emp_of_month(work_hours)

print result