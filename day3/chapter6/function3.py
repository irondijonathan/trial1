def add(num1, num2):
    print(num1 + num2)


def addition(num1, num2):
    return num1 + num2


add(5, 6)
print("Couldn't Print function with a return value: ")
addition(10, 5)
print("Can now print function with a return value", addition(10, 5))

if add(5, 6) == 11:
    print('Yayy!!!!!')

if addition(10, 5) == 15:
    print('Yayy!!!!!')



