# def hello():
#     print("Hello world")

# hello()

# def greetings(salute, name):
#     print(f'good {salute} mr.{name}')

# greetings('morning', 'Ben')
# greetings('Afternoon', 'Jonathan')
# greetings('evening', 'Joshua')


# def addnum(num1,num2):
#     result  = num1 + num2
#     print(f'the answer is {result}')

# addnum(2,4)
# addnum(1293,343)

# def areaOfTriangle(base, height):
#     area = ((1/2)*int(base) *int(height))
#     print(f'the area is {area}')

# areaOfTriangle(200, 300)
# areaOfTriangle(100, 200)
# areaOfTriangle(100, 50)



#printing even numbers
def printEven(start, stop):
    while start <= stop:
        if start % 2 == 0:
            print(start)
        start += 1


print('1 - 20')
printEven(1,10000)

# print('6 to 20')
# printEven(6, 20)

# go and learn about default value parameter
# also understand how value returning funvtions carry out their tasks
#global variable
