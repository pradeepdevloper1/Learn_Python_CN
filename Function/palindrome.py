def reverse(n):
    rev=0   
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev

def checkPalindrome(num):
    if(reverse(num)==num):
        return True
    else:
        return False
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
