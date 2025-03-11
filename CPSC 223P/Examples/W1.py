# external notes:
# if "python --version" does not work in the terminal, you cannot run this file from the actual terminal
# you must reinstall the most recent version of python and try again
# if, even then, it still does not work, inquire with the professor (and send a screenshot of the error) 
# for further help

# you can run individual python codes in terminal
# to run code from a file, use the "play button" in the top right of vscode


print("hello world")

age = 20
# age = 30 (*)
# if the code snippet above (*) is included, age will be reassigned to 30 (from 20)
print(age)

name = input("What is your name?")
# prints out prompt and waits for user to input
# note: input will not work unless it is assigned to some variable
print(name)

birth_year = int(input("What is your birth year?"))
age = 2025 - birth_year
# The code snippet above will result in an error if the input type is not defined as int (in either declaration of birth year or age).
# The reason is due to the assignment of birth year as a string and then its usage as a integer.
# print(birth_year)
print(age)

course = "python programming"
print(course.find("y"))
# the code snippet above will print out the index of the letter y in "course" (1)
print(course.find("program"))
# this prints out the index of the first letter of "program" in course (if the word is present)
print(course.lower())
# print(course.upper())
# this prints the string in lower/upper case
print(course.strip())
# this removes spaces at both ends of the string (i any exist)
course = "python programming with anrudh"
print(course.split())
# this splits the string in half
print(course.replace("anrudh", "sahu"))
# this replaces "anrudh" in course with "sahu"