def factorial_recursive(n):
    if(n==0): return 1
    else:
        return n * factorial_recursive(n-1)
number = int(input("Enter the number you want to evaluate factorial for: "))
print(f"Factorial of {number} is: {factorial_recursive(number)}")


