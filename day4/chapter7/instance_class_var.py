class Employee():
    pay_raise = 0.10

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        increment = self.pay_raise * self.p
        return increment + self.p

e1 = Employee('Benedict', 'Uwazie', 2000)
e1.f = 'Slim'
print(e1.f)
print(e1.salary())

e2 = Employee('Alabi', 'Adebayo', 3000)
print(e2.salary())