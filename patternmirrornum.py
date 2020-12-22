## Read input as specified in the question
## Print the required output in given format
n=int(input())
if 0<=n<=50:
    i=1
    while i<=n:
        spaces=1
        while spaces<=n-i:
            print(' ',end='')
            spaces+=1
        num=1
        num2=1
        while num<=i:
            print(num,end='')
            num+=1
            num2+=1     
        print()
        i+=1