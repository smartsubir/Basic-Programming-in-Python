def fib(a,b):
  if (b==0):
    return a
  else:
    return fib(b , a%b)
ass = fib(100,2000)
print(ass)