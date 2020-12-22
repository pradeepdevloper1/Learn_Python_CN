n=int(input())
i=1
while i<=n:
    j=1
    startchar=chr(ord('A')+i-1)
    while j<=n:
        print(chr(ord(startchar)+j-1),end='')
        j+=1
    print()    
    i+=1    