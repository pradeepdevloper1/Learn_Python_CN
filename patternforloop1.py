n=int(input())
for i in range(1,n+1,1):
    for j in range(1,i,1):
        print(' ',end='')
    for k in range(i,n+1,1):
        print(k,end='')
    print()  
for i in range(2,n+1,1):
    for j in range(1,n-i+1,1):
        print(' ',end='')
    for k in range(n-i+1,n+1,1):
        print(k,end='')
    print()       
