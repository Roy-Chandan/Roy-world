def user_choice():
    
    choice = 'Wrong'
    accept_range = range(0,10)
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        
        choice = input ("Enter a number between 1-10: ")
        
        if choice.isdigit() == False:
            print ("Please enter a number not string")
            
        if choice.isdigit() == True:
            if int(choice) in accept_range:
                within_range = True
            else:
                print ("Number is not between 1-10")
                within_range = False
                
                
    return int(choice)
        
    


result = user_choice()
print (result)
