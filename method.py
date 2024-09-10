'''class maths:
    def add(self,a,b,c):
        self.z=a+b+c
        return self.z

t=maths()
print("Total: ",t.add(3,4,5))'''

class maths:
    def __init__(self):
        self.x=10
        self.y=20
        self.z=self.x+self.y

t = maths()
print("Total: ",t.z)
          
