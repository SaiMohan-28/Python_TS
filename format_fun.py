'''
format() it returns a formatted representation of the given value
controlled by the format specifier

format(value,"format_specifier")
'''
a="TS"
print("Hi {0} {1}".format(a).format(a))
#Hi TS TS

a="TS"
b="INDIA"
print("Hi {0} {1}".format(a).format(b))
#Hi TS TS

a="TS"
#b="INDIA"
print("Hi {0}".format(a))
#Hi TS

a="2"
b='1'
print("Hi {0}".format(b))
#Hi 1


z="{a} {b}".format(a="TS",b="INDIA")
print(z)

y="TS"
print("{0}".format(y))


p="{0} {1}".format("TS","INdia")
print(p)


print("{0} {1}".format("TS","INdia"))

print("{1} {0}".format("TS","INdia"))

print("{} {}".format("TS","INdia"))


