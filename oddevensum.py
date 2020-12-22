## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
num=int(input())
evensum=0
oddsum=0
while num>0:
    rem=num%10
    if rem%2==0:
        evensum+=rem
    oddsum+=rem 
    num=num//10
    
print(str(evensum)+'\t'+str(oddsum))