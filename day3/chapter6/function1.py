def hello():
    print('Hello people')


hello()

def greeting(salute, name):
    print(f'Good {salute}, Mr. {name}')

greeting('Morning', 'Ben')
greeting('Night', 'Alabi')
greeting('Evening', 'Joshua')

def add(num1, num2):
    add = num1 + num2
    print(add)

add(5, 7)
add(12, 20)

def area_triangle(height, base):
    area = 0.5 * base * height
    print(area)

area_triangle(50, 100)
area_triangle(100, 200)
area_triangle(200, 300)