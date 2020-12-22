n=int(input())

def isPrime(n):
    for d in range(2,n,1):
        if(n % d == 0):
            break
        else:
            return True
        return False  

ans=isPrime(n)
print(ans)