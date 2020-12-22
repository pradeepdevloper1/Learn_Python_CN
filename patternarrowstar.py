n=int(input())
if n%2!=0:
    n=n//2+1
    i=1
    while i<=n:
        j=1
        while j<i: 
            print(' ',end='')
            j+=1
        k=1    
        while k<=i:
            print('*',end=' ')
            k+=1
        print()
        i+=1
    i=1
    while i<n:
        j=1
        while j<n-i:
            print(' ',end='')
            j+=1
        k=1
        while k<=n-i: 
            print('*',end=' ')
            k+=1
        print()
        i+=1   