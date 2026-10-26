print("This program checks if a year is a leap year or not.")

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


print("Using nested if-else statements:")

year = int(input("Enter a year: "))

if year % 4!= 0:
    print(year, "is not a leap year.")
else:
    if year % 100!= 0:
        print(year, "is a leap year.")
    else:
        if year % 400!= 0:
            print(year, "is not a leap year.")
        else:
            print(year, "is a leap year.")   


print("Using elif statements:")

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a leap year.")
elif year % 100 == 0:
    print(year, "is not a leap year.")
elif year % 4 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")