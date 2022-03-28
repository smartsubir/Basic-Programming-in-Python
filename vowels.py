w=input("Enter a word: ")
count=0
v=['a','e','i','o','u','A','E','I','O','U']
for i in w:
    if i in v:
        count+=1
print(f"there are total {count} vowels.")       