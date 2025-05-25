class Animal:
    def __str__(self):
        name = type(self).__name__
        return name
    def eat(self):
        print(f'{str(self)} is eating')
    def sleep(self):
        print(f'{str(self)} is sleeping')

class Dog(Animal):
    def speek(self):
        print('Woof\n')

class Cat(Animal):
    def speek(self):
        print('Meows\n')

class Sheep(Animal):
    def speek(self):
        print('Baa\n')

class Cow(Animal):
    def speek(self):
        print('Moo\n')

d = Dog()
print(d)
d.eat(); d.sleep(); d.speek()

c = Cat()
print(c)
c.eat(); c.sleep(); c.speek()

sh = Sheep()
print(sh)
sh.eat(); sh.sleep(); sh.speek()

co = Cow()
print(co)
co.eat(); co.sleep(); co.speek()