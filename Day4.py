# friends= ["Alice","Bob","Charlie"," diane","eve"]

# for name in friends:
#     print(f"Hello, {name}")

#     print("How are you")


# fruits=["apple","mango","orange"]

# for fruit in fruits:
#     upper=fruit.upper()
#     length=len(fruit)

#     print(f"{upper}-{length} letters")

# print("Done")

# for i in range (1,10):

#     print(f"{i*5}")

# names=["Ram", "Hari", "shyam","Gita"]

# print(len(names))

# for i in range(len(names)):
#     print("index of this name is : ",i)
#     print(names[i])

# bucket=[1,2,3,4,5]

# sum=0

# for value in bucket:
#     sum=sum+value
#     # print(sum)
#     print(f"The value at this loop is: {value}")
#     print(f"The sum up to this point is: {sum}")
#     print("\n")

# number=1

# while number<=10:
#     print(number)
#     number= number+1              #it stop to print while the number is in 11

# answer= input("Password: ")

# while answer!= "Keshab":
#     print("Wrong password! Try again")
#     answer=input("password: ")

# print("Correct password")

# for i in range(1,4,1):
#     for j in range(10,14,1):
#         print(i)


# for i in range(1,4,1):
#     print("the value of i is:",i)
#     for j in range(10,14,1):
#        print("The value of j is:",j)

# rows=6
# for i in range (1,rows+1):
#     for j in range(i,):
#         print("⭐", end=" ")
#     print()

# students = ["Alice","Bob","Charlie"]

# # # Manual way (range + index)
# # for i in range(len(students)):
# #     print(f"{i}: {students[i]}")

# # Cleaner way — enumerate()
# for i, name in enumerate(students, start=1):
#     print(f"Seat {i}: {name}")