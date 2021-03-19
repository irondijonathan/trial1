
#create a class called product
#determine what the class variable for the product class will be
#and create an innit method with three
#parameters for the product class, create another method 
#that will calculate the discount prize for each product
#call three times


#create a child class called shirt
#add new parameters that will be a list of size in the 
#innit method of the child class. craete a method that dislay information about this shirt
#class.
#access the attritutes on this child class



class product():
    discont_percent = 0.10

    def __init__(self, product_name, product_ID, price):
        self.n = product_name
        self.pro = product_ID
        self.p = price

    def discount_meth(self):
        new_price = self.p - (self.p * self.discont_percent)
        return new_price




p1 = product('Apple', 'iphone X', 3000)
print(p1.discount_meth())

p2 = product('Samsung', 'Samsung_A20', 1000)
print(p1.discount_meth())

p3 = product('Techno', 'Techno_R7', 500)
print(p3.discount_meth())



class shirt(product):
    def __init__(self, product_name, product_ID, price, size):
        super.__init__(product_name, product_ID, price)
        self.s = size

    def diplayInfo(self):
        print('product_name: ' self.n)
        print('product_ID: ' self.pro)
        print('price: ' self.p)

    
s1 = shirt('trouser', 'channel', 300, ['LG', 'XL', 'SM'] )

s1.discount_meth()

print('sizes below')
print(s1.s)

print('looing through the sizes')
for s in s1.s:
    print(s)

print('printing the second item')
print(s1.s[1])
        

