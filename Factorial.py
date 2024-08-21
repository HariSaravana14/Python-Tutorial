i = 1
x = 1

while(i<=3):
    x = x*i
    i = i+1
i = 1
y = 1
while(i<=2):
    y = y*i
    i = i+1

total = x/y
print("Result",total)



print("----------------------------------")

def fact(a):
    i = 1
    j = 1
    while(i <= a):
        j *= i
        i += 1
    return j

x = int(input("Enter the Value of X: "))
y = int(input("Enter the Value of Y: "))
print("Result: ",fact(x)/fact(y))


print("----------------------------------")


def fact(n):
    g = 1
    i = 1
    while(i<=n):
        g = g*i
        i+= 1
    return g

x = int(input("Value of x"))
j = 1
sum = 0
while(j<=x):
    sum = sum+fact(j)
    j = j+1
return sum
print("Result: ",sum)
