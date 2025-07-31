def add(P, Q):
    #This function is used for adding two numbers 
    return P + Q
def substract(P, Q):
    #This function is used for substracting two numbers 
    return P - Q
def multiply(P, Q):
    #This function is used for multiplying two numbers 
    return P * Q
def divide(P, Q):
    #This function is used for dividing two numbers 
    return P / Q

# Now we will take input from the user
print ("Please select the operation.")
print ("a. Add")
print ("b. Substract")
print ("c. multiply")
print ("d. divide")

choice = input("Please enter choice (a/ b/ c/ d): ")

num_1 = int (input("Please enter the first number: "))
num_2 = int (input("Please enter the second number: "))

if choice == 'a':
    print (num_1, " + ", num_2, " = ", add(num_1,num_2))

elif choice == 'b':
    print (num_1, " - ", num_2, " = ", substract(num_1,num_2))

elif choice == 'c':
    print (num_1, " * ", num_2, " = ", multiply(num_1,num_2))      

elif choice == 'd':
    print (num_1, " / ", num_2, " = ", divide(num_1,num_2))      
else:
    print("This is an inavalid input")    