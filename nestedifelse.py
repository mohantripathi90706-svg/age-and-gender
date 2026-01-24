
a = int(input("enter your age :"))
b = input("enter your gender :")
if a>=18 :
    if b=="male" or "Male" :
        print("ADULT MALE")
    elif b=="female" or "Female" :
        print("ADULT FEMALE")
    else :
        print("Invalid Input")
else :
    print("You are a MINOR")