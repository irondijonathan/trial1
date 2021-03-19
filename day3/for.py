southEast = ['Abia', 'Imo', 'Enugu', 'Anambra', 'Ebonyi']

# for state in southEast:
    # print(state)




# num = int(input("enter the number: "))
# for x in range(1, 12):
    
    # print(f'{x} X {num} = {x*num}')
    


# number = int(input("enter the number: "))
# y = 0
# for (y < 12):
#     answer = number * x
#     print(f'{number} X {y} = {answer}')
#     x += 1


south_East = {
    'Abia' : 'Umuahia',
    'Imo' : 'Owerri',
    'Enugu' : 'Enugu',
    'Anambra' : 'Oka',
    'Ebonyi' : 'Abakiliki'
}

for s in south_East:
    print(f'{s}, {south_East[s]} ')

print("printing values")

for s in south_East.values():
    print(s)


print("printing keys")
for s in south_East.keys():
    print(s)

print("keys,value")
for s in south_East.items():
    print(s)