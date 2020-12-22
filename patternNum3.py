n=int(input())
if n<=0:
    print()
else:
    print(1)
    i=1
    while i<n:
        j=0
        while j<=i:
            if(j==0 or j==i  ):
                print(1,end='')
            else:
                print(2,end='')
            j+=1  
        i+=1  
        print()