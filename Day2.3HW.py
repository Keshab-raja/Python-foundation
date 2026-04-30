# TASK 1: Rectangle Maths
# Given length = 8 and width = 5,
# calculate and print the AREA and PERIMETER.
# Area      = length × width
# Perimeter = 2 × (length + width)
# length = 8
# width = 5

# Write your code below:

# Area= length * width

# print(f"Area is", Area)

# perimeter=2*(length + width)

# print(f"Perimeter is", perimeter)


    # TASK 2: Sharing Candies (Floor Division + Modulus)
# You have 47 candies to share equally among 5 friends.
# Using //  find how many each friend gets.
# Using %   find how many candies are left over.
# Print: "Each friend gets [x] candies, with [y] left over!"
# total_candies = 47
# friends = 5

# # Write your code below:
# # Using //  find how many each friend gets.
# Each_friends_get= total_candies//friends

# # print(Each_friends_get)

# # Using %   find how many candies are left over.
# candy_left= total_candies%friends
# # print(candy_left)

# print(f"Each friends get {Each_friends_get} candies, with {candy_left} left over!.")

# TASK 3: User Input Calculator
# Ask the user for two whole numbers.
# Print their sum, difference, product, and quotient.
# (Remember to convert input to int!)
# Write your code below:

# Num1=int(input("Enter the first number: "))
# Num2= int(input("Enter the second number: "))

# sum=Num1+Num2
# diff= Num1-Num2
# product= Num1*Num2
# quotient= Num1/Num2

# print(f"Sum is {sum}")
# print(f"The diff is {diff}")
# print(f"product is {product}")
# print(f"quotient is {quotient}")
# print(type(Num1))
# print(type(Num2))


# TASK 4: Price Calculator
# Ask the user:
#   - How many items they want to buy  (use int())
#   - The price per item               (use float())
# Calculate the total cost and print it.
# Write your code below:

# Iteams=int(input("How many items you want to buy: "))


# price=float(input("Enter the price per items: "))

# Total_cost= Iteams*price

# print(f"Total cost is {Total_cost}")
# print(type(Iteams))

# ⭐ BONUS CHALLENGE: Temperature Converter
# Ask the user for a temperature in Celsius.
# Convert it to Fahrenheit with this formula: F = (C × 9/5) + 32
# Print: "[C]°C is equal to [F]°F"
# (Hint: use float() for the input so decimal values work too!)
# Write your code below:

Current_temperature= float(input("Enter the current temperature in celsius: "))

fahrenheit= (Current_temperature*9//5)+32

print(F"The temperature of {Current_temperature} degree celsius is equal to {fahrenheit}")