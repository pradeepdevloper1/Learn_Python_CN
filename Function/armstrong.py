def armstrong(n):
    rev=0   
    while n>0:
        rem=n%10
        rev=rev+rem**3
        n=n//10
    return rev

def checkArmstrong(num):
    if(armstrong(num)==num):
        return True
    else:
        return False
num = int(input())
isArmstrong = checkArmstrong(num)
if(isArmstrong):
	print('true')
else:
	print('false')
