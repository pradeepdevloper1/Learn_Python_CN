## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
print('-----'+chr(ord('A')-1+n))
while i<=n:
    j=1
    startchar=chr(ord('A')-1+n-i+1)
    while j<=i:
        print(chr(ord(startchar)-1+j),end='')
        j+=1
    print()    
    i+=1    