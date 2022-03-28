n=input("Enter a number: ")
e,o=0,0
for i in range(len(n)):
    if int(n[i])%2==0:
        e+=int(n[i])
    else:
        o+=int(n[i])
print("sum of even number is: %d"%e)
print("sum of odd number is: %d"%o)