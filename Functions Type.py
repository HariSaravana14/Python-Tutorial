#function type 1
print("Function Type 1 no argument and no return value")
def display():
    print("Welcome")
print("ABD") 
display()
print("Bye")

print("-------------------------------------------------------------")

print("Function Type 2 argument and no return value")
# function type 2
def sum(a,b):
    c = a+b
    print("Result: ",c)

sum(2,4)


print("-------------------------------------------------------------")

print("Function Type 3 no argument and return value")
# function type 3

def square(f):
    c = f*f
    return c
print("Result: ",square(4))


print("-------------------------------------------------------------")

print("Function Type 4 no argument and return value")
# Function Type 4

def square():
    t = 2*3
    return t
s = square()
print("Result: ",s)
