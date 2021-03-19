state = {
    'southEast' : ['Abia', 'Imo', 'Enugu', 'Anambra', 'Ebonyi'],
    'southWest' : ['Lagos', 'Ondo', 'Oyo', 'Osun', 'Ogun'],
    'northWest' : ['Zamfara', 'Jigawa', 'Kano', 'Sokoto',]
}

# loopong through the dictionary and the list in them

for zones in state:
    print(zones.upper())
    for s in state[zones]:
        print(s)