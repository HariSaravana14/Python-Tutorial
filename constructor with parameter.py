'''class a:
    def one(self):
        self.f=10

    def two(self):
        self.k=20
    def three(self):
        self.j=40

r=a()
r.one()
r.two()
r.three()
print(r.f)
print(r.k)
print(r.j)'''


'''class student:
    def input_master(self):
        self.adno=int(input("adno: "))
        self.name=(input("name: "))
        self.address=input("Address: ")

s=student()
s.input_master()
print("adno",s.adno)
print("name",s.name)
print("address",s.address)'''

'''class student:
    def __init__(self):
        self.adno=int(input("adno: "))
        self.name=(input("name: "))
        self.address=input("Address: ")

t=[]
t.append(student())
t.append(student())
t.append(student())
for r in t:
    print("adno: ",r.adno)
    print("name: ",r.name)
    print("address: ",r.address)'''


'''class a:
    b=10
    
print(a.b)'''



class a:
    b=10
    def access(self):
        print(b)

t=a()
n=a()
print("a.b",a.b)
print(t.b)
print(n.b)

