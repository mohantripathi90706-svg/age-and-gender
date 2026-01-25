a = int(input("enter the year :"))
if a%4==0 :
    if a%100!=0 :
        print("It Is a LEAP YEAR")
    else :
        if a%100==0 :
            if a%400==0 :
                print("LEAP YEAR")
            else :
                print("not a leap year")
        else :
            print("leap year")
else :
    print("NOT A LEAP YEAR")