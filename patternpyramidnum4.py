#test
n=int(input())
if 0<=n<=50:
    i=1
    while i<=n:
        spaces=1
        num1=1
        while num1<=i:
            print(num1,end='')
            num1+=1
        space=2*n-2*i
        while space>0:
            print(' ',end='')
            space=space-1
        num2=i
        while num2>=1:
            print(num2,end='')
            num2-=1
        print()
        i+=1