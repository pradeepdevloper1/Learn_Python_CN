
s=int(input())
e=int(input())
w=int(input())
f=s
c=0
while f<=e:
    c=int((f-32)*(5/9))
    print(str(f)+"\t"+str(c));
    f+=w
