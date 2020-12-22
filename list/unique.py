n=int(input())
while(n!=0):
    terms=int(input())
    li = [int(li) for li in input().split()]
    for x in li:
        y = li.count(x)
        if y==1:
            print(x)
            break
        
    n = n-1