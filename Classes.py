class Person():
    def __init__(self, name = 'Spartacus'):
        self.name = name
    def sayHello(self):
        print("Hi!")
    def sayMyName(self):
        print(f'I\'m {self.name}')
        self.__changeName()
    def __changeName(self):
        if self.name != 'Spartacus':
            self.name = 'Spartacus'

plato = Person('Plato')
anon = Person()

anon.sayHello()
anon.sayMyName()
plato.sayMyName()
plato.sayMyName()


class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x},{self.y})'
    def __str__(self):
        return f'This is a Point(x,y) object, set at point ({self.x}, {self.y})'
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

p1=Point(1,2)
p2= Point(5.5,6.6)
p3 = p1+p2
print (p3)



class MobilePhone():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def __eq__(self, other):
        if self.brand == other.brand and self.model == other.model and self.price == other.price:
            return True
        else: return False
    def __repr__(self):
        return f'MobilePhone({self.brand}, {self.model}, {self.price})'
    def __str__(self):
        return f'\nObject of class MobilePhone: \nBrand: {self.brand}\nModel: {self.model}\nPrice: {self.price}\$'
    def __add__(self, other):
        return self.price+other.price
    def __gt__(self, other):
        return self.price > other.price
    def __lt__(self, other):
        def __gt__(self, other):
            return self.price < other.price
lgOne = MobilePhone('LG', "One...?", 1000)
samS8 = MobilePhone('Samsung', "S8", 1500)
samS8s = MobilePhone('Samsung', "S8", 1500)


print (lgOne == samS8)
print (samS8 == samS8s)
print(samS8s+lgOne)
print (samS8s>lgOne)
