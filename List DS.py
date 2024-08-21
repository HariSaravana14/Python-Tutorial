a = ["orange","rose","red"]
a.append("Green")
print(a)


a=[]
for i in range(1,10):
    a.append(i)

print(a)


a=[]
n = int(input("Enter How many students: "))
i = 0
while(i<n):
    name = input("Name: ")
    a.append(name)
    i=i+1

print(a)
