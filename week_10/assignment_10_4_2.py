from week_10.Settings import Settings

# Run this code this, first you'll get two questions and half way through the first run you'll get another.
# During the second run you shouldn't get any questions since your previous answers have been saved to "settings.txt"
settings = Settings(["name", "favourite_star_wars_character"])

print("Hello", settings.get("name"))
print("I really like", settings.get("favourite_star_wars_character"), "too.")
print("I'm not so sure about", settings.get("favourite_star_trek_character"), "though, I hope you don't mind?")
