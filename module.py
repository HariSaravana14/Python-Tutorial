import mymodule
x = int(input("Entre the Value: "))
t=0
i=1
while(i<=x):
    t = t+mymodule.fact(i)
    i=i+1
print("result: ",t)




