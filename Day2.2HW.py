# TASK 1: Upper, Lower, Title
# Create a variable with your full name (first + last).
# Print it in UPPERCASE, lowercase, and Title Case.

first_name="keshab "
middle_name= "raj "
last_name="Adhikari "
full_name = first_name + middle_name + last_name
# print(f"My name is: {full_name}")

# # Write your three print statements below:
# upper_case= full_name.upper()
# lowercase= full_name.lower()
# title= full_name.title()

# print(upper_case)
# print(lowercase)
# print(title)


# TASK 2: String Length
# Using the full_name variable from Task 1,
# print exactly: "My name has [number] characters!"
# (Use len() — do NOT count manually!)
# Write your code below:

# print("My name has number:", len(full_name))
# print(f"My name has {len(full_name)} characters ")

# TASK 3: F-String Introduction
# Fill in these variables, then write ONE f-string that says:
# "Hi! I'm [name], I'm [age] years old, and I love [hobby]!"
# name = "Keshab"
# age = 28 
# hobby = "travel"

# # Write your f-string print below:

# print(f"Hi! I'm {name}, I'm {age} years old, and I love {hobby}.")

# TASK 4: Name Banner
# Print a line of 32 "=" signs, then your name, then 32 "=" signs again.
# Use the * operator — no copy-pasting!
# Write your code below:

# print("=" *32)
# print("Keshab")
# print("=" *32)

# TASK 5: Input + F-String
# Ask the user for their favorite animal.
# Then print: "Wow, [animal] is a great choice! 🐾"
# Write your code below:

# favorite_animal= input("Please type your favourite animal: ")
# print(f"wow, {favorite_animal} is a great choice. ")

# ⭐ BONUS CHALLENGE:
# Ask the user to type their name.
# Print their name in UPPERCASE, sandwiched between ★ symbols.
# Example output: "★★★ ALICE ★★★"
# Hint: you will need .upper() and the + operator.
# Write your code below:

name= input("Enter your name: ")
operator="⭐"*3

print(operator,name.upper(),operator)