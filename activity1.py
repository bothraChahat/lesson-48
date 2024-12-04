#Polymorphism Implementation
#class dog
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        return"i am {} and my age is {}  year".format(self.name,self.age)
    
    def make_sound(self):
        return"I bark at the strangers"
    
d=dog("siro",3)
print(d.info())
print(d.make_sound())

#class cat
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        return"I am {} and my age is {}  year".format(self.name,self.age)
    
    def make_sound(self):
        return"I make sound meow"
    
c=cat("lilly",1)
print(c.info())
print(c.make_sound())