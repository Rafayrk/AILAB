
check=int(input("Enter Year\t"))
if (check%4)==0:
    if(check%100)==0:
        if(check%400)==0 :
            print("The year is a leap year (it has 366 days)")
        else:
            print("The year is not  leap year")
    else :
        print("The year is a leap year (it has 366 days)")
else :
        print("The year is not  leap year ")

