'''class sequence_series:
    def fact(self,n):
        p = 1
        i =1
        while(i<=n):
            p= p*i
            i = i+1
        return p
    def natural(self, n):
        p = 0
        i = 1
        while(i<=n):
            p = p+i
            i=i+1
        return p

r = sequence_series()
t=  int(input("Value of t: "))
print("result",r.fact(t))
print("result",r.natural(t))'''
 

#using method
'''class a:
    def one(self):
        self.x=10

t =a()
t.one()
k=a()
k.one()
g=a()
g.one()
print(t.x+k.x+g.x)'''


#using default constructor
'''class a:
    def __init__(self):
        self.x=10

t =a()
k=a()
g=a()
print(t.x+k.x+g.x)'''


class a:
    def __init__(self):
        self.x=10

t=a()
k=t
print(t.x+k.x)
























