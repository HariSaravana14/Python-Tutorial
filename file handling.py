import file1
'''i=1
while(i<=1):
    status = int(input("Do you want to exit press key 3 or continue the process to press any key number: "))
    if(status==3):
        break
    else:
        empno = input("empno: ")
        empname=input("empname: ")
        address=input("address: ")
        city= input("City: ")
        phone_no=input("phone no: ")
        file1.write(empno,empname,address,city,phone_no)'''

f=open("d:\\Python\\filehandle.txt","r")
c = f.read()
print(c)
