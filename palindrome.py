def checkPalindrome(num):
#Implement Your Code Here
    rever=0
    num2=num
    while (num>0):
        rem=num%10
        rever=(rever*10)+rem
        num=num//10
    if(rever==num2):
        return True


		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
