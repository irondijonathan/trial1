person = ['benedict', 45, True, 'fair']
print(person[0])

print(f'my name is {person[0]}, I am {person[1]}years old and {person[3]} in complexion')

#adding item to a list
person.append('Developer')
print(person)



#changing item in a list
person[2] = False
print(person)


#adding item @ a aspecified index

person.insert(1, 'darkhair')
print(person)


#class excerice

userlogin = ['jonathan', '1234567']

password = input('enter new password ')
confirmPassword = input('confim password ')

if len(password) < 7:
    print('pasword is too short')
elif password == confirmPassword:
    userlogin[1] = password
    print(userlogin)
elif password != confirmPassword:
    print('passwords do not match')
else:
    print('invalid operation')