a=input("enter a string")
b=input("enter a string")
if a in b:
    c=b.replace(a,"my name is")
    print(c)
else:
    print(a not in b)


