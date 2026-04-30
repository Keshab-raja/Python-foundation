# ---------------------------------------------------------
# HOMEWORK 1: FOR LOOP BASICS 🔄
# ---------------------------------------------------------


# TASK 1: Your Favourite Things
# Create a list of 5 things you like (foods, games, anything!).
# Use a for loop to print each one on its own line like this:
# "I really like: pizza"
# Write your code below:

Favourite_things=["Foods","Games","songs","Travel","play"]
for favourite in Favourite_things:     # when i use for loop it take 1/1 data and print it.
    print(f"I really like {favourite}.")


# TASK 2: Length Reporter
# Create a list of at least 5 words.
# Loop through the list and for each word print:
# "banana → 6 letters"
# Hint: use len() inside the loop.
# Write your code below:
Fruits=["Banana","Orange","Apple","Mango","Watermelon"]
for fruit in Fruits:
    length=len(fruit)
    print(f"{fruit} - {length} Letters")




# TASK 3: Shopping Bill
# Create a list of at least 5 item prices (as numbers).
# Loop through them and print each price, then after the loop
# print the total.
# Use the accumulator pattern: start total = 0, add each price.
# Write your code below:

Prices=[52,0,60,500,200,100,80]
total=0
for price in Prices:
    total+=price
print(f"Total price: Rs. {total}")   # if we put it on loop it will show each step total price



# ⭐ BONUS CHALLENGE:
# Create a list of temperatures in Celsius:
# [0, 20, 37, 100, -10]
# Loop through and convert each to Fahrenheit: F = (C × 9/5) + 32
# Print: "0°C = 32.0°F"
# Write your code below:

Temp=[0,20,37,100,-10]

for temperature in Temp:
    fahrenheit=(temperature*9/5)+32  # formula for converting degree celsiou to fernheit
    print(f"{temperature}°C = {fahrenheit}°F")
