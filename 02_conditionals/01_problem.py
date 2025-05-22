age = int(input("Enter your age as integer:"))

if age<=0:
    print("Invalid age integer")
elif age<=13:
    print("Child")
elif age<=19:
    print("Teen")
elif age<=59:
    print("Adult")
else:
    print("Senior Citizen")
    
    