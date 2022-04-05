year = int(input("Enter a year: ")) #Taking in the users input
numb = int(input("Enter number of years: "))

cal = year + numb   #adding year and the number of years

for year in range (year,cal):   #initiating for loop in range of year to (cal)culation
    if year % 4 == 0:       #if  year modulus 4 is equal to 0 print...
        print(str(year) + " is a leap year")
    else:       #if year modulus 4 is not equal to zero print...
        print(str(year) + " is not a leap year")
