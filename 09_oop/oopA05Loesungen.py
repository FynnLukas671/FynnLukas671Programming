class Animal():
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('Animal makes a sound')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return 'Dog makes a sound'

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return 'Cat makes a sound'

d1 = Dog('Jim')
c1 = Cat('Cat')

print(d1.sound(), c1.sound())