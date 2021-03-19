class Car():
    doors = 4
    wheels = 4

   
    def details(self, name, color):
        return f'the car"s name is {name} and the color is {color} with {self.wheels} wheels and {self.doors} doors'


c1 = Car()
print(c1.doors)
print(c1.wheels)
print(c1.details('BMW', 'Black'))

c2 = Car()
print(c2.details('Toyota', 'Red'))