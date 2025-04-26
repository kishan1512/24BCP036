def p3():
    a=input("enter a string")
    countalp=0
    countdig=0

    for ch in a:
        if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
            countalp=countalp+1

        else:
            countdig=countdig+1


    print(countalp)
    print(countdig)


p3()