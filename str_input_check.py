str1=input("Enter the first string: ")
str2=input("Enter the first string: ")
li1=str1.upper()
li2=str2.upper()
if li2 in li1:
    print("{} contains {}".format(str1,str2))
else:
    print("{} doesn't contain {}".format(str1,str2))
    