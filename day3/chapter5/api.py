

# 'South East'
#     'Imo'
#     'Imo'
#     'Imo'
#     'Imo'
# 'South West'
#     'Imo'
#     'Imo'
#     'Imo'
#     'Imo'

states = {
    'South East': ['Imo', 'Abia', 'Enugu', 'Anambra'],
    'South West': ['Lagos', 'Ondo', 'Oyo', 'Osun'],
    'Nort West': ['Zamfara', 'Jigawa', 'Kano', 'Sokoto'],
}

print(states['South West'][0])
for zones in states:
    print(zones)
    for s in states[zones]:
        print(s)

