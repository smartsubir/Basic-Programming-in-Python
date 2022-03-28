str1=input()
str2=input()
set1= sorted(str1)
set2= sorted(str2)
if set1==set2:
    print("It is an anagram")
else:
    print("It is not an anagram")