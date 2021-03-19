num = int(input('enter a number: '))
x = 0
while x < 12:
    x += 1
    print(f'{num} X {x} = {num * x}')



number = [10,20,30,40,50]
total = 0
x = 0
while x < len(number):
    total += number[x]
    x += 1
print(f'total = {total}')
average = total/len(number)
print(f'average = {average}')
