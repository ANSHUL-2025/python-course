try:
    num1, num2 = eval(input("Enter two numbers, seperated by comma : "))
    result = num1/num2
    #using multiple except block for different type of error

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1,except:2")

except:
    print("wrong input")

else:
    print("No exception")

finally:
    print("This will execute no matter what")        

