def getEvenNumber(number):
    if number % 2 == 0:
        return True
    else:
        return False
evenNumber = list(filter(getEvenNumber, range(40)))
print(evenNumber)


num = [0,1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,1,234,56,68,90,98]
evenNumber2 = list(filter(getEvenNumber, num))
print(evenNumber2)

evenNumber3 = list(filter(lambda n: True if (n % 2 == 0) else False, num ))
print(evenNumber3)



#.............................................................MAP FUNCTION

def addingANumberToItself(n):
    n += n
    return n


double = list(map(addingANumberToItself, range(30)))
print(double)


def exponent(n):
    n = n**3
    return n

expo = list(map(exponent, range(20)))
print(expo)

expo4 = list(map(lambda n : n**4, range(10)))
print(expo4)