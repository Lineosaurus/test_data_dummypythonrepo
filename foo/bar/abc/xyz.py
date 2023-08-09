# PhD Adventure Python Script

# Define a list of research topics
research_topics = ["quantum physics", "neuroscience", "astrophysics", "artificial intelligence", "climate change"]

# Choose a research topic to explore
chosen_topic = input("Choose a research topic to explore: ")

# Check if the chosen topic is in the list
if chosen_topic.lower() in research_topics:
    print(f"Embark on a journey to uncover the mysteries of {chosen_topic}!")

    # Ask about a specific aspect of the research
    aspect = input("What specific aspect of your research intrigues you? ")
    print(f"Delve deep into the realm of {chosen_topic} and explore {aspect}.")

    # Share an interesting finding
    print(f"Discover a fascinating connection between {aspect} and the world of {chosen_topic}.")
else:
    print("That's an interesting choice! Each research topic offers unique insights.")

print("Happy exploring, future PhD!")
