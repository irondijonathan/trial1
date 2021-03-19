# x = 1
# while x <= 20:
#     if x % 2 == 0:
#         print(x)
#     x += 1

def print_even(start, stop):
    while start <= stop:
        if start % 2 == 0:
            print(start)
        start += 1

print('1 to 10')
print_even(1, 10)
print('6 to 16')
print_even(6, 16)


def office(name, color='Yellow'):
    print(f'The color of {name} is {color}')


def my_office(color='Yellow'):
    print(f'The color of my office is {color}')


my_office()
my_office('Green')
office('MTN')
office('Alabian', 'Sky Blue')


def print_even_default(stop, start=1):
    while start <= stop:
        if start % 2 == 0:
            print(start)
        start += 1


print('2 to 16')
print_even_default(12)
print('4 to 15')
print_even_default(16, 4)

