n=int(input("Enter a number: "))
d=True
for i in range(2,n):
    if n%i==0:
        d=False
        break
if d:
    print("prime")
else:
    print("non Prime")
