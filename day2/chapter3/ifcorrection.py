# Write a program that displays an error message if username is wrong 
# or another error message if password is wrong 
# and then a success message if both are correct


username = input('Enter username: ')
password = input('Enter password: ')

db_username = 'benedict'
db_password = 'pass1234'

if username != db_username:
    print('Username is wrong')
elif password != db_password:
    print('Password is wrong')
elif username == db_username and password == db_password:
    print('Username and password is correct')

