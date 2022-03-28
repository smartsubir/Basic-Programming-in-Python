n=input("enter the 4 digit number :")
a=0
if (len(n)==4):
    for i in range (len(n)):
        a=a+int(n[i])
        i+=i
    print("{}+{}+{}+{}={}".format(n[0],n[1],n[2],n[3],a)) 
else:
    print ("you input is not a 4 digit number")
