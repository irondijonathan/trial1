class Car():
    doors = 4
    wheels = 4

    def __init__(self):
        print('This ia a constructor')

    def details(self, name, color):
        return f'the car"s name is {name} and the color is {color} with {self.wheels} wheels and {self.doors} doors'

c1 = Car()