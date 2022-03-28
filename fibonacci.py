v=int(input("Enter a range: "))
a=0
b=1
print(a)
print(b)
for i in range(v):
    sum=a+b
    a=b
    b=sum
    print(sum)