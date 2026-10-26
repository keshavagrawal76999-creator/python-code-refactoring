# Intentionally hard-to-read example for comparison only.
def f(a):
 x=0
 for i in a:
  if i>0:x=x+i
 return x

if __name__ == "__main__": print(f([2,-3,4,0]))
