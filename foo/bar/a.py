# Kid's Adventure Python Script

# Define a list of magical creatures
magical_creatures = ["unicorn", "dragon", "fairy", "mermaid", "griffin"]

# Choose a magical creature to go on an adventure with
chosen_creature = input("Pick a magical creature to go on an adventure with: ")

# Check if the chosen creature is magical
if chosen_creature in magical_creatures:
    print(f"Let's go on a magical adventure with a {chosen_creature}!")
    
    # Ask where the adventure should take place
    adventure_place = input("Where should our adventure take place? ")
    print(f"Great! Our adventure with the {chosen_creature} will take place in {adventure_place}.")
    
    # Describe the adventure
    print(f"Get ready for an exciting adventure with the {chosen_creature} in the land of {adventure_place}!")
else:
    print("That's a fantastic choice! Every creature is special and unique.")

print("Have a magical day!")
