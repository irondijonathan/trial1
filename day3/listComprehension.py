numbers = []

for n in range(1,30):
    numbers.append(n)
print(numbers)

print("using list comprehensiom")

number = [n for n in range(1,12)]
print(number)

evenNumber = [n for n in range(1,1000000) if n % 2 == 0 ]
print(evenNumber)