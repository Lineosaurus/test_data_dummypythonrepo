# Kids' Theme Python Script

# Define a list of favorite animals
favorite_animals = ["elephant", "lion", "dolphin", "penguin", "kangaroo"]

# Print a fun animal fact
def print_fun_fact(animal):
    fun_facts = {
        "elephant": "Elephants can weigh as much as 22 cars!",
        "lion": "Lions are the kings of the jungle.",
        "dolphin": "Dolphins are super smart and love to play.",
        "penguin": "Penguins waddle around and slide on their bellies.",
        "kangaroo": "Kangaroos have strong legs and hop all over the place!"
    }
    if animal in fun_facts:
        print(f"Fun Fact about {animal.capitalize()}: {fun_facts[animal]}")
    else:
        print(f"Sorry, I don't have a fun fact about {animal}.")

# Ask the user for their favorite animal
user_favorite = input("What's your favorite animal? ")

# Print a personalized message
if user_favorite in favorite_animals:
    print(f"Wow, {user_favorite} is a cool choice!")
    print_fun_fact(user_favorite)
else:
    print("Nice choice! Every animal is unique and special.")

print("Have a great day!")
