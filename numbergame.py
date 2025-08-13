import random #importing module
playing = True #initialise
number = str(random.randint(0,5)) 

print("I will generate a number from 0 to 5, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
#iterate loop till the condition is true
while playing:
    guess = input("Give me your best guees! \n")
    if number == guess:
        print("You win the game")
        print("The number was",number)
        break

    else:
        print("your guess isn't quite right, try again. \n")