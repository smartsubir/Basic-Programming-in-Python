a=int(input("Enter the first value: "))
b=int(input("Enter the second value: "))
print("Choose a number to perfom the follwing task\n1.add\n2.sub\n3.expo\n4.mul")
op=int(input())
if op==1:
    print(a+b)
elif op==2:
    print(a-b)
elif op==3:
    print(a**b)
elif op==4:
    print(a*b)
else:
    print("invalid input")