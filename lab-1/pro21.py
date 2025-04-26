#calculate net salary
a=float(input("enter value of gross salary"))
b=float(input("enter value of allowance"))
c=float(input("enter value of deduction"))
c=(a*10)/100
b=(c*3)/100
net_salary=a+b-c
print(net_salary)
