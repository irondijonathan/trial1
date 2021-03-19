import modules

d1 = Developer('Irondi', 'Jonathan', 5000, 'Python')
print(d1.finalEmail)

d2 = Developer('col', 'jon', 8000, 'Javascript')
print(d2.finalEmail)




e1 = Employee('Benedict', 'Uwazie', 2000)
e1.f = 'Slim'
print(e1.f)
print(e1.salary())