a = lambda x :x+5
print(a(2))

b = lambda a,b :a+b
print(b(2,3))

c= lambda a,b : a if (a*a) else b
print(c(2,5))
 
lst=[1,2,3,4,5]
l=list(map(lambda x : x+5,lst))
print(l)

lst=[4,5,6,7,8]
sqr=list(map(lambda y: y*y,lst))
print(sqr)
from  functools import reduce
lst=[1,2,3,4,5,6]
y= reduce(lambda x,y:x+y,lst)
print(y)
