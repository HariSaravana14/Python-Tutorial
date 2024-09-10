def fact(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
        i = i+1
    return s

n = int(input("Enter the Number: "))
print(fact(n))
