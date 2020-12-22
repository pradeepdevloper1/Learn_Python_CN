def getInput():
    v1=int(input())
    v2=int(input())
    return v1,v2

def add():
    x,y=getInput()
    return x+y
def sub():
    x,y=getInput()
    return x-y
def multiply():
    x,y=getInput()
    return x*y
def divide():
    x,y=getInput()
    return x/y
def remainder():
    x,y=getInput()
    return x%y
def empty():
    return '' 
def invalid():
    return 'Invalid Operation'   

choice=int(input())
operation=[add,sub,multiply,divide,remainder,empty,invalid]
output=operation[choice-1]()
print(output) 


