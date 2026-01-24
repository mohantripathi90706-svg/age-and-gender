a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
c = int(input("enter the third number :"))
if a>b and a>c and b>c:
    print("a is GREATEST")
elif b>c and b>a and c>a:
        print("b is GREATEST")
elif c>a and c>b and a>b:
        print("c is GREATEST")