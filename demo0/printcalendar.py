import calendar

def mycal(month, year):
    print(calendar.month_name[month], " ", year)
    print("Mo", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    for i in range(0, calendar.monthrange(year, month)[0]) :
        print("    ", end="")
    j = 1
    for i in range(calendar.monthrange(year, month)[0] + 1, calendar.monthrange(year, month)[1] + 1 + calendar.monthrange(year, month)[0]):
        if j < 10:
            print (j, "  ", end="")
        else: 
            print (j, " ", end="")
        j += 1
        if i % 7 == 0:
            print("")
    
while 1:
    try:
        month = int(input("Give the month: ")) 
        if month < 1 or month > 12:
            raise Exception("Enter a valid month")
        year = int(input("Give the year: "))
        if year < 1:
            raise Exception("Enter a valid year")
        break
    except Exception as e:
        print(str(e))

mycal(month, year)