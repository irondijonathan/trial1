account = ['irondicjonathan@gmail.com', '1234567']
#first collect the email you wish to verify from the user
email = input('enter your email: ')

if email in account:
    password = input('enter new password ')
    confirmPassword = input('confim password ')

    if len(password) < 7:
            print('pasword is too short')
    elif password == confirmPassword:
        account[1] = password
        print(account)
        print("password has been changed succesfully")
    elif password != confirmPassword:
        print('passwords do not match')
    else:
        print('invalid operation')
elif email == "":
    print("please enter an email")
else:
    print("email does not exist in the database")