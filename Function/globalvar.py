a=20
def func1():
    global a
    a=30
    print(a)
    print(id(a))

print(a)
print(id(a))
func1()
print(a)
print(id(a))