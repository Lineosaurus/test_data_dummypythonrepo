# Dummy Python Script

# Lists of colors and numbers
colors = ["red", "green", "blue"]
numbers = [1, 2, 3, 4, 5]

# Dictionary of information
person = {
    "name": "John",
    "age": 30,
    "occupation": "Developer"
}

# Print the colors
print("Colors:")
for color in colors:
    print(color)

# Print the even numbers
print("\nEven Numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)

# Print person's information
print("\nPerson:")
print("Name:", person["name"])
print("Age:", person["age"])
print("Occupation:", person["occupation"])
