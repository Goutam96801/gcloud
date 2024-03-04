def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input
number = int(input("Enter a number: "))

# Check if the number is odd or even
result = check_odd_even(number)

# Output
print(f"The number {number} is {result}.")

