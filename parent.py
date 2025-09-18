class dad:
    
    def __init__(self, eyes , aggresive):
        self.eyes = eyes
        self.aggresive = aggresive

    def dislpay(self):
        print("your eye color is",self.eyes)
        print("you are aggresive",self.aggresive) 

class son(dad):

    def __init__(self, name, age, eyes, aggresive):
        self.name = name
        self.age = age

        super().__init__(eyes,aggresive)

obj = son("penguin",8,"blue", True)

obj.dislpay()
