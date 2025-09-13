class fruit:
    # class variable
    taste = 'Sweet'

    # instance variable
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Object Creation
apple = fruit('Apple', 'Red')
banana = fruit('Banana', 'Yellow')
grapes = fruit('grapes', 'green')

print(apple.taste)
print(apple.name, apple.color)
print(banana.name, banana.color)
print(grapes.name, grapes.color)
