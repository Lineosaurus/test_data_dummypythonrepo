# Dummy Python Script

# Function to calculate the square of a number
def square(number):
    return number ** 2

# List of names
names = ["Alice", "Bob", "Charlie"]

# Print a welcome message
print("Welcome to the Dummy Python Script!")

# Calculate and print squares of numbers
for i in range(1, 6):
    squared = square(i)
    print(f"The square of {i} is {squared}")

# Print the list of names
print("Names:")
for name in names:
    print(name)

# Calculate and print the sum of numbers
numbers = [10, 20, 30, 40, 50]
sum_of_numbers = sum(numbers)
print(f"The sum of numbers is {sum_of_numbers}")

# Say goodbye
print("Goodbye from the Dummy Python Script!")
