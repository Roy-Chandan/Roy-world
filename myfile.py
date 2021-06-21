
myfile = open('myfile.txt')

#myfile.read()


#move the cusror to the initial location
#myfile.seek()

#myfile.readlines()



with open('myfile.txt') as var:
	content = var.read()



print(content)



with open('myfile.txt',mode='r') as var:
	print (var.read())



with open('myfile.txt',mode='a') as var:
	var.write ('This is the Fourth line')
	


print (content)