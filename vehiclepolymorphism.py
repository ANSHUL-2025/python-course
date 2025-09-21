class BMW:
    def start(self):
        return "BMW is starting with a burble shot..."
    
    def stop(self):
        return "BMW has stopped gracefully."
    
    def speed(self):
        return "BMW top speed is 250 km/h."


class Ferrari:
    def start(self):
        return "Ferrari is starting with a thunderous roar!"
    
    def stop(self):
        return "Ferrari screeches to a halt."
    
    def speed(self):
        return "Ferrari top speed is 340 km/h."


# Polymorphism in action
def car_details(car):
    print(car.start())
    print(car.speed())
    print(car.stop())
    print("-" * 40)


# Create objects
bmw = BMW()
ferrari = Ferrari()

# Using polymorphism
for car in (bmw, ferrari):
    car_details(car)
