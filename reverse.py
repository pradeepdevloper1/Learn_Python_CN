
def reverse(n):
    rever=0
    while (n>0):
        rem=n%10
        rever=(rever*10)+rem
        n=n//10
    return rever
#Implement Your Code He

n=int(input())
result = reverse(n)
print(result)