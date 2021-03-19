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
    def __init__(self, first_name, last_name, pay, prog_lang):
        super(). __init__(first_name, last_name, pay)
        self.prog = prog_lang
        self.email = f'{self.f}C{self.l}@gmail.com'
        self.finalEmail = self.email.lower()


    
    def staffDetail(self):
        return f'firstname: {self.f}, lastname: {self.l}'





class Employee():
    pay_raise = 0.10

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        increment = self.pay_raise * self.p
        return increment + self.p