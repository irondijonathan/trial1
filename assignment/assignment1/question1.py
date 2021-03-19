score = int(input('enter your score: '))

if score > 100 or score < 0:
    print('invalid score')

elif score > 1 and score <= 34:
    print('you failed')

elif score >= 35 and score <= 44:
    print('pass')

elif score >= 45 and score <= 49:
    print('fair')

elif score >= 50 and score <= 59:
    print('good')

elif score >= 60 and score <= 69:
    print('very good')

else:
    print('excellent')