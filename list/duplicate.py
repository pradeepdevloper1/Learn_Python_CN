import sys
def duplicateNumber(arr, n) :
    for x in li:
        if x not in unique_list:
             unique_list.append(x)


def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0 :
        return list(), 0
    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n

#main
t = int(sys.stdin.readline().strip())
while t > 0 :    
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1
    