def display_all(*q):
    for a in q:
        print(a)

f = []
i = 1
while(i<=5):
    k = input("Name: ")
    f.append(k)
    i = i+1
display_all(f)
