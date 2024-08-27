'''class maths:
    def square(self,a):
         b=a*a
        return b

m = maths()
n= maths()
r=m.square(2)+n.square(3)
print("result:",r)'''




'''class maths:
    def square(self,a):
        b=a*a
        return b
    def sum(self,x,y):
        h=x+y
        print("Sum",h)

m = maths()
print(m.square(10))
m.sum(2,3)'''



class maths:
    def add(self):
        self.a=int(input("Value of A: "))
        self.b=int(input("Value of B: "))
        c = self.a+self.b
        return c

m = maths()
print(m.add())
        
