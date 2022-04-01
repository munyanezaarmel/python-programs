from math import*
a=int(input("ENTER FIRST NUMBER"))
b=int(input("ENTER SECOND NUMBER"))
c=int(input("ENTER THIRD NUMBER"))
D=b*b-4*a*c
print(f"chech if it is in the correct form{a}x`2+{b}y+{c}")
if D>0:
 x1=b +(math.sqrt(D)/2*a)
print(f'the first number is {x1}')
print(f'the the second  number is {x2}')
 elif D==0:
x1=b/2*a
print(f"the first number is equal to the second number{x}")
else:
print('delta is equal to zero')




