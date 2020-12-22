
def checkMember(n):
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
    pass

n=int(input())
nterms = 100
if(checkMember(n)):
    print("true")
else:
    print("false")