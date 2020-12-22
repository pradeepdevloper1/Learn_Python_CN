n=int(input())
i=1
while i<=n:
    j=n
    while j>=i:
        if i%2==0:
            print(0,end=' ')
        else:
            print(1,end=' ')
        j-=1
    print()
    i+=1        