#Encapsulation Implementation
class computer:
    def __init__(self):
        self.__maxprice=900

    def sell(self):
        return"the selling price is",self.__maxprice
    
    def setmaxprice(self,price):
        self.__maxprice=price
        return"max price is",self.__maxprice
    
c=computer()
print(c.sell())

c.__maxprice=1000
print(c.sell())

c.setmaxprice(1000)
print(c.sell())