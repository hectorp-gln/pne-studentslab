text = "  Hello, World! Welcome to Python Programming.  "

#The string with leading and trailing spaces removed (use strip())

stripped = text.strip()
print("Stripped:", stripped)

# number of words in the string (use split())

print("Word count:", len(text.split()))

#The string with the first letter of each word capitalized (use title())


print("Title Case:",text.strip().title())

#Whether the stripped string starts with "Hello" (use startswith())

print("Starts with Hello:", stripped.startswith("Hello"))

#Whether the stripped string ends with "ing." (use endswith())

print("Ends with ing.:", stripped.endswith("ing."))

#The position (index) of the word "Python" in the stripped string (use find())

print("Python position:", stripped.find("Python"))

#The words joined back together separated by " - " (use split() and " - ".join())

print("Joined:", " - ".join(text.split()))
