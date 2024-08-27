def write(*store):
    f=open("d:\\Python\\filehandle.txt","a")
    for inputt in store: 
        f.write(inputt)
    f.close()
