def digits():
    a=int(input("Enter a number"))
    if a<10:
        print(a,"is one digit number")
    elif a<100:
        print(a,"is two digit number")
    else:
        print(a,"is multipul digit number")


digits()
