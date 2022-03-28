s=input("s= ")
stack=[]
br={'(':')','{':'}','[':']'}
for char in s:
    if char in ['(','{','[']:
        stack.append(char)
    elif stack:
        top=stack.pop()
        if br[top] == char:
            print ("True")
        else:
            print("false")


