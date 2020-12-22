## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
sum=0
li = [int(li) for li in input().split()]
for i in li[0:]:
    sum+=i
print(sum)