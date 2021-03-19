#this is kinda like converting a string to an integer

age = 23
convert_age = str(age)

print ('my name is Jonathan and i am '+str(age)+' years old')
print ('my name is Jonathan and i am '+convert_age+' years old')

name = "Benedict"
noOfChildren = 4
state = "Chicago"
salary = 2500.55

print('my name is '+name+', from '+state+' and married with '+str(noOfChildren)+' children and i earn '+str(salary)+' as salary')

print('i am {}, from {} and married with {} children and i earn {} as salary'.format(name,state,noOfChildren,salary))
print(f'i am {name}, from {state} and married with {noOfChildren} children and i earn {salary} as salary')