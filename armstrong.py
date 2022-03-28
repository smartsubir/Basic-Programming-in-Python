n=int(input("Enter a number: "))
m=n
a=0
while(n>10):
    p=n%10
    a=a+p**3
    n=n//10
a=a+n**3
if a==m:
    print(f"{m} is a armstrong number.")
else:
    print(f"{m} is not a armstrong number.")