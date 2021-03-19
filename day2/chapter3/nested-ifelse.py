name1="ben"
name2="be^&74345"
# print(name.isalpha())

if name1.isalpha():
    if len(name1) > 5:
        print('Hello people')
    else:
        print('Your character is less than 5')
else:
    print('Your data is not an alphabet')


# Write a program that displays a success message 
# if username and password is correct and an error
# message if username and password is wrong

# username = 'benedict'
# password = 'pass12345'

username = input('Enter Username: ')
password = input('Enter Password: ')

db_username = 'benedict'
db_password = 'pass12345'

if username.lower() == db_username and password.lower() == db_password:
    print('Username and password is correct')
else:
    print('Username is wrong')




