day = input("Enter the Day of the Week: ")
age = int(input("Enter the age in Integer: "))

#-------------------CONVENTIONAL--------------------------
# if day == "Wednesday":
#     if age<=0:
#         print("Invalid age was Entered")
#     elif age<18:
#         print("As today is Wednesday the discounted price for children will be $6")
#     else: print("As today is Wednesday the discounted price for adults will be $10")
# else:
#     if age<=0:
#         print("Invalid age was Entered")
#     elif age<18:
#         print("Price for children will be $8")
#     else: print("Price for adults will be $12")

#-----------------------NEW--------------------------------------

# if day=="Wednesday":
#     price = 10 if age>=18 else 6
#     print("As today is Wednesday the discounted price will be:", price)
# else: 
#     price = 12 if age>=18 else 8
#     print("Price will be:",price) 

#--------------------LESSER CODE SAME FUNC-----------------------

price = 12 if age>=18 else 8

if day=="Wednesday": 
    price -=2
    print("The Discounted price is:",price)
print("Price will be:", price)