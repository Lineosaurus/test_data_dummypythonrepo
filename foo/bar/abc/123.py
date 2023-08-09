# Dark Fantasy Python Script

# List of dark creatures
dark_creatures = ["vampire", "witch", "werewolf", "demon", "ghost"]

# Choose a dark creature to encounter
chosen_creature = input("Enter the name of a dark creature you'd like to encounter: ")

# Check if the chosen creature is in the list
if chosen_creature.lower() in dark_creatures:
    print(f"You've entered the realm of {chosen_creature}s.")

    # Ask if the user wants to face the creature
    choice = input(f"Do you dare to face the {chosen_creature}? (yes/no): ")
    if choice.lower() == "yes":
        print(f"You've challenged the {chosen_creature} and lived to tell the tale.")
    else:
        print("Wise choice. Sometimes the shadows hold secrets best left unexplored.")
else:
    print("This realm is filled with mysterious beings, and your imagination is the limit.")

print("Venture cautiously into the darkness.")
