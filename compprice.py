class Computer:

    def __init__(self):
        self.__maxprice = 955

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()                
c.sell()

c.__maxprice = 1089
c.sell()

c.setMaxPrice(1089)
c.sell()