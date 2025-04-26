print("the co-ordinates of center is (0,0)")
x1=float(input("enter value of x1"))
y1=float(input("enter value of y1"))
r=float(input("enter value of radius"))
if (x1*2+y1*2)>r*2:
    print("point lies outside the circle")
elif (x1*2+y1*2)<r*2:
    print("point lies inside the circle")
else:
    print("point lies on the circle")



