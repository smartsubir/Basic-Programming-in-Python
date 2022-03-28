v=int(input("Enter the total numbers of vahicals: "))
w=int(input("Enter the total numbers of wheels: "))
if w%2==1 or w<2 or w<=v or v*4<w or v*2>w:
    print("INVALID INPUT")
else:
    x=v-((w//2) -v)
    print("TW={a} FW={b}".format(a=x,b=v-x))