import random

class FruitQuiz:
    # Create a constructor
    def __init__(self):
        # Create a dictionary of fruits as keys and color as values
        self.fruits = {
            'apple': 'red',
            'orange': 'orange',
            'watermelon': 'green',
            'banana': 'yellow'}
        

    # Function for the quiz, a fruit will be chosen randomly
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            
            print("What is the colour of {}".format(fruit))
            user_answer = input()

            if user_answer.lower() == color:
                print("Correct answer")
            else:
                print("Wrong answer ")

            option = int(input("Enter 0, if you want to play again, otherwise enter 1: "))
            if option :
                break

print("Welcome to Fruit Quiz")
fq = FruitQuiz()
fq.quiz()