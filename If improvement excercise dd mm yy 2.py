#Jarod Pierre Murton
#if inprovement excercise
#30/09/14

date = input("Please enter your date of birth in dd/mm/yy: ")

day = date[0:2]
month = date[3:5]
year = date[6:8]

if day == "01" or day == "21" or day == "31":
    day_after = "st"
elif day == "02" or day == "22":
    day_after = "nd"
elif day == "03" or day == "23":
    day_after = "rd"
else:
    day_after = "th"

if month == "01":
    month = "January"
elif month == "02":
    month = "February"
elif month == "03":
    month = "March"
elif month == "04":
    month = "April"
elif month == "05":
    month = "May"
elif month == "06":
    month = "June"
elif month == "07":
    month = "July"
elif month == "08":
    month = "August"
elif month == "09":
    month = "September"
elif month == "10":
    month = "October"
elif month == "11":
    month = "November"
elif month == "12":
    month == "December"
else:
    print("Invalid number")

if year > "30":
    century = "19"
else:
    century = "20"

print("{0}{1} {2} {3}{4}".format(day,day_after,month,century,year))
