import math
class calci():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return(self.a-self.b)
    def mul(self):
        return(self.a*self.b)
    def div(self):
        return(self.a/self.b)
    def po(self):
        return  math.pow(a,b)
class scical():
    def __init__(self,a):
        self.a=a
    def si(self):
        return math.sin(self.a)
    def asin(self):
        return math.sinh(self.a)
    def co(self):
        return math.cos(self.a)
    def aco(self):
        return math.cosh(self.a)
    def ta(self):
        return math.tan(self.a)
    def ata(self):
        return math.tanh(self.a)
    def cosec(self):
        return math.asin(self.a)
    def se(self):
        return math.acos(self.a)
    def ct(self):
        return math.atan(self.a)
q=int(input("Enter 1 if you want to perform arithematic operations \nEnter 2 if you want to perform trignomertric operations \n"))

if q==1:
    a = float(input("Enter 1st no."))
    b = float(input("Enter 2nd no."))
    ob1 = calci(a,b)
    while True:
        print(" 0 . Exit\n 1 .Addition\n 2 .Substraction\n 3 .Multiplication\n 4 .Division\n 5 .power")
        c=int(input("Your choice"))
        if c==0:
            break
        elif c==1:
            print(ob1.add())
            print()
        elif c==2:
            print(ob1.sub())
            print()
        elif c==3:
            print(ob1.mul())
            print()
        elif c==4:
            print(ob1.div())
            print()
        elif c==5:
            print(ob1.po())
            print()
        else:
            print("Invalid choice")
            print()
elif q==2:
    a = float(input("Enter the num: "))
    while True:
        ob2 = scical(a)
        print(" 0 . Exit\n 1 .sine\n 2 .sine inverse\n 3 .cos\n 4 .cos inverse\n 5 .tangent\n 6 .tangent inverse\n 7 .cosine\n 8 .secant\n 9 .cot")
        c = int(input("Your choice"))
        if c==0:
            break
        elif c==1:
            print(ob2.si())
            print()
        elif c==2:
            print(ob2.asin())
            print()
        elif c==3:
            print(ob2.co())
            print()
        elif c==4:
            print(ob2.aco())
            print()
        elif c==5:
            print(ob2.ta())
            print()
        elif c==6:
            print(ob2.ata())
            print()
        elif c==7:
            print(ob2.cosec())
            print()
        elif c==8:
            print(ob2.se())
            print()
        elif c==9:
            print(ob2.ct())
            print()
        else:
            print("Invalid")
            print()
else:
    print("Invalid")