
n = int(input("enter a number to get it's factorial: "))
m=n
a=n
while(n>1):
    a=a*(n-1)
    n=n-1
print("the factorial of {m} is {a}".format(m=m,a=a))