# A. Numbers
# multiply 2 numbers and then divide by another
print("Input 2 numbers to multiply: ")
mult1 = int(input("First input: "))
mult2 = int(input("Second input: "))
multiplication = mult1 * mult2
# print("Result: ", multiplication)
denominator = int(input("Input a number to divide by: "))
division = multiplication / denominator
print("Result: ", division)

# determine the remainder
remainder = multiplication % denominator
print("Remainder: ", remainder)

# square and cube numbers
square = int(input("Input a number to square: "))
square = square ** 2
print("Result: ", square)
cube = int(input("Input a number to cube: "))
cube = pow(cube, 3)
print("Result: ", cube)


# B. Strings
# obtain name
name = input("Input your name: ")

# seperate name into first and last names
first_name, last_name = name.split()
print("First name: ", first_name)
print("Last name: ", last_name)

# uppercase and lowercase a string
uppercase = name.upper()
print("Uppercase: ", uppercase)
lowercase = name.lower()
print("Lowercase: ", lowercase)

# reverse a string
reverse = name[::-1]
print("Reverse: ", reverse)


# C. Lists
# create a list of 5 elements
foods = []
print("Input 5 foods: ")
food = input("Food: ")
foods.append(food)
food = input("Food: ")
foods.append(food)
food = input("Food: ")
foods.append(food)
food = input("Food: ")
foods.append(food)
food = input("Food: ")
foods.append(food)
print(foods)

# print the first and last elements
first = foods[0]
print("First Food: ", first)
size = len(foods)
last_position = size - 1
last = foods[last_position]
print("Last Food: ", last)

# input two more elements
print("Input 2 more foods: ")
food = input("Food: ")
foods.append(food)
food = input("Food: ")
foods.append(food)
print(foods)

# remove a element
print("Removing the 4th food")
foods.pop(3)
print(foods)

# sort the list alphabetically
print("Alphabetically Sorted: ")
foods.sort()
print(foods)