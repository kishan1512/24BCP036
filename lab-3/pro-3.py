a=input("enter a string1")
b=input("enter a string2")
if a in b:
    print(a,"in",b)
elif b in a:
    print(b,"in",a)
else:
    print(a!=b)
    