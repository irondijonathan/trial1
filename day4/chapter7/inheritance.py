class Employee():
    pay_raise = 0.10

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        increment = self.pay_raise * self.p
        return increment + self.p


class Developer(Employee):
    pass

    def staffDetail(self):
        return f'firstname: {self.f}, lastname: {self.l}'

d1 = Developer('Jonathan', 'Irondi', 5000)
print(d1.staffDetail())
print(d1.f)
print(d1.salary())

d2 = Developer('Ransome', 'Kuti', 9000)
print(d2.staffDetail())
print(d2.f)
print(d2.salary())