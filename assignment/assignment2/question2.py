names = ['Jonathan','James', 'Jane', 'Joan', 'Jamal', 'Jennifer']
x = 0
newName = input('enter the name you wish to veify ')
while x <= len(names)-1:
   
    if newName.lower() == names[x].lower():
        print(f'Name is already registered at position {x}')
    else:
        print(f'Name is not registered at position{x}')
    
    x += 1

#                                                        OR

if newName in names:
    print('it exists in the database ')
else:
    print ("It doesn't exixst in the database")
    
#note: this does not support manipulation of the lower and uppercase of the list
    
       
    
    
    