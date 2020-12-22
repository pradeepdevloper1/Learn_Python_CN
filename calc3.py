while True:
    choice=int(input())
    if choice==1:
        a=int(input())
        b=int(input())
        print(a+b)
    elif choice==2:
        a=int(input())
        b=int(input())
        print(a-b)
    elif choice==3:
        a=int(input())
        b=int(input())
        print(a*b)
    elif choice==4:
        a=int(input())
        b=int(input())
        print(a//b)
    elif choice==5:
        a=int(input())
        b=int(input())
        print(a%b)
    elif choice==6:
        break
    else:
        print("Invalid Operation")