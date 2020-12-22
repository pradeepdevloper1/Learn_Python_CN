n=int(input())
k=2
while k<=n:
    Flag =False;
    d=2;
    while d<k:
        if k%d==0:
            Flag=True
        d+=1;
    if not(Flag):
        print(k)
    k+=1;    