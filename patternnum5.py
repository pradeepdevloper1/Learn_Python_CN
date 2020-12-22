## Read input as specified in the question
## Print the required output in given format
n=int(input())
if 0<=n<=50:      
    i=1
    while i<=n:
        j=1
        while j<=i:
            print(j,end='')
            j+=1
        print()    
        i+=1    