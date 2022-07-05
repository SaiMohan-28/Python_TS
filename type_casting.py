'''
#Explicit
a=5
print(type(a))

b=float(5)
print(b)
print(type(b))

c=complex(2,5)
print(c)

d=str(c)
print(d)

#implicit

a=10
b=12.0
c=a+b
print(c)
'''

a=(input())
b=int(a)#input to integer
print(b)

f=12.3
print(int(f))

c=True
print(int(c))

s=100
print(chr(s))#takes value and gives ASCII

x='A'#returns constant integer value of specified character
print(ord(x))
print(ord('a'))

s='65'
print(float(s))

t='23.3456789'
print(float(t))
