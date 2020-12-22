n=int(input())
nterms = 100

def fib(n):
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print(nterms)
        print(n1)
    else:
        while count < nterms:
            if(n1==n):
                return True
            else:
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
            return False    
output=fib(n)
print(output)
if(output==True):
    print("true")
else:
    print("false")    

