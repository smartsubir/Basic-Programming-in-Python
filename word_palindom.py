n=input("Enter the string: ")
stk=[]
for i in range(len(n)):
    if n[i]in stk:
        stk.remove(n[i])
    else:
        stk.append(n[i])
if len(n)%2==0 and len(stk)==0:
    print("ok")
elif len(n)%2!=0 and len(stk)==1:
    print("ok")
else:
    print("no")
