south_east = ['Imo', 'Abia', 'Anambra', 'Enugu', 'Ebonyi']

for state in south_east:
    print(state)

for n in range(6):
    print(n)
print('BREAK')
for n in range(2, 6):
    print(n)

print('Break')
number = 3
for n in range(1, 13):
    result = number * n
    print(f'{number} X {n} = {result}')

states = {
    'Imo':'Owerri',
    'Lagos':'Ikeja',
    'Osun':'Oshogbo',
    'Oyo':'Ibadan',
    'Ondo':'Akure'
}

for s in states:
    print(f'Key: {s}, Value: {states[s]}')

print('PRINTING VALUES')
for s in states.values():
    print(s)

print('PRINTING KEYS')
for s in states.keys():
    print(s)

print('PRINTING KEYS, VALUES')
for x, y in states.items():
    print(x, y)
