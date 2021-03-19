def kwargs(**kwargs):
    print(kwargs)

kwargs(key1 = 'value1', key2 = 'value2', key3 = 'value3')


def state_Capital(**kwargs):
    for state, capital in kwargs.items():
        print(f'The capital of {state} is {capital}')


state_Capital(
    imo = 'owerri',
    lagos = 'ikeja',
    rivers = 'portharcourt',
    niger = 'minna'
    )