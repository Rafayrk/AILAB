year = int(input("Enter a number: "))
# Python program to check if the input year is a leap year or not



# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("a leap year")
       else:
           print("leap yea")
   else:
       print("leap year")
else:
   print("leap year")


