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

d1 = Developer('Irondi', 'Jonathan', 5000, 'Python')
print(d1.finalEmail)

d2 = Developer('col', 'jon', 8000, 'Javascript')
print(d2.finalEmail)















#create a class called product
#determine what the class variable for the product class will be
#and create an innit method with three method
#parameters for the product class, create another method 
#that will calculate the discount prize for each product
#call three times


#create a child class called shirt
#add new parameters that will be a list of size in the 
#innit method of the child class. craete a method that dislay information about this shirt
#class.
#access the attritutes on this child class
#