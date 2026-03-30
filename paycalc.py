def computepay(hours, rate):
    if hours <= 40:
        hourly = hours * rate
    else:
        ot = hours - 40
        hourly = 40 * rate + ot * rate * 1.5
    return hourly
hours = input("Enter Hours: ")
try:
    hours = float(hours)
except:
    print("ERROR, please enter numeric input!")
    exit()
rate = input("Enter Hourly Pay Rate: ")
try:
    rate = float(rate)  
except:
    print("ERROR, please enter numeric input!")
    exit()
pay = computepay(hours,rate)
print(pay)
input('Press ENTER to exit')
#next course is gonna be to add a graphical ui :)