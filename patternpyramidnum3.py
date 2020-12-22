n=int(input())
if 0<=n<=50:
    i=1
    while i<=n:
        spaces=1
        while spaces<=n-i:
            print(' ',end='')
            spaces+=1
        num1=1
        num2=i
        while num1<=i:
            print(num2,end='')
            num1+=1
            num2-=1
        num1=1
        num2=2
        while num1<=i-1:
            print(num2,end='')
            num2+=1
            num1+=1         
        print()
        i+=1