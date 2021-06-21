
def cube(n):

	res = []

	for x in range(n):
		res.append(x**3)

	return res


print (cube(6))


# use yield as generator


def cube_gen(n):

	for x in range(n):
		yield x**3

#print (cube_gen(8))

for x in cube_gen(8):
	print (x)



