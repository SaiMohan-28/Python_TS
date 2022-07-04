
x='abc'
def fun():
    print(x,"def")
fun()
#abc def


x='abc'
def fun():
    print("def",x)
fun()
#def abc

x='abc'
def fun():
    print("def"+x)
fun()
#defabc


x='abc'
def fun():
    x='def'
    print("def"+x)
fun()
print(x)
#defdef
#abc



def fun():
    global x
    x=1
    print(x)
fun()
print(x)


z=10
def abc():
    global z
    z=12
    print(z)
abc()
print(z)
#12
#12

z=10
def abc():
    z=12
    print(z)
abc()
print(z)
#12
#10





