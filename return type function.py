def square(r):
    t = r*r
    return t

def sum(a,b):
    c = a+b
    return square(c)

print(sum(3,2))



def list_all(*d):
    print(d[1])

list_all("red","rose")




def list_all(a,b):
    inn = a
    while (inn<=b):
        print("Roll no",inn)
        inn = inn+1

i = int(input("Enter initial rollno: "))
f = int(input("Enter final rollno: "))
list_all(i,f)

















