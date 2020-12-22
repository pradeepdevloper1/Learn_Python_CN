def printTable(start,end,step):
    for f in range(start,end+1,step):
        c=int((f-32)*(5/9));
        output=str(f)+" "+str(c)
        print(output)
    pass    
      
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)