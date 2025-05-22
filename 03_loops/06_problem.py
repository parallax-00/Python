number = int(input("Enter the number you want to calculate factorial for: "))
fact=1
while number>0:
    fact=fact*number
    number= number-1
print(f"Factorial is: {fact}")