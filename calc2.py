choice = int(input())
num1 = int(input())
num2 = int(input())

def  func(num1,num2):
    if choice == 1:
            return num1+num2

    elif choice == 2:
            return num1- num2

    elif choice == 3:
            return  num1* num2

    elif choice == 4:
            return num1/ num2

    elif choice == 5:
            return num1% num2        
    elif choice == 6:
            return
    elif choice==7:
            return "Invalid Input"
res=func(num1,num2)
print(res)            