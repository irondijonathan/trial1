# name1 = 'be'
# name2 = 'rfkl9@@@'

# if name1.isalpha():
#     if len(name1) > 5:
#         print('Hello')
#     else:
#         print('your character is less than 5')
# else:
#     print('your data is not an alphabet')


userlogin = 'Jonathan'
paswordlogin = '10856672'

username = input('enter your user username  ')

if username.lower() == userlogin.lower():
    password = input('enter your password  ')
    if password == paswordlogin:
        print("you've logged in succesfully!!")
    else:
        print('invalid password')
else:
    print('invalid username')