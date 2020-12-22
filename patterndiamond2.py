num=int(input())
r=1
while r<=num:
    c=1
    while c<=r:
        print(c,end='')
        c+=1
    print()
    r+=1
r=1    
while r<=num:
    c=1
    space=1
    while space<=num:
        print(' ',end='')
        space+=1
    while c<=r:
        print(c,end='')
        c+=1
    print()
    r+=1    