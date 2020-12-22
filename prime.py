n=int(input())
i=2
Flag=False;
while i<=n-1:
    if n%i==0:
        Flag=True
    i+=1;

if Flag==True:
    print('Not Prime')
else:
    print('Prime')    