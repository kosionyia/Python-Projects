# Part A — Basic Syntax & Variables
# Exercise 1 — Declare and Print Variables
instructor_name = "Cletus"
students_in_p_class = 20
course_name = "Python Programming"
print(f"The instructor is {instructor_name}, there are {students_in_p_class} students in the class, and the course name is {course_name}!")

# Exercise 2 — Swap Two Variables Without a Third Variable
students_morning = 15
students_evening = 25
print(f"Before swapping: Morning class has {students_morning} students, Evening class has {students_evening} students.")
students_morning, students_evening = students_evening, students_morning
print(f"After swapping: Morning class has {students_morning} students, Evening class has {students_evening} students.")

# Exercise 3 — Assign Multiple Variables in One Line
python, java, ai = 25, 28, 12
print(f"Python = {python}, Java = {java}, AI = {ai}")

# Exercise 4 — Check the Type of a Variable
age = 25
course_rating = 3.2
course_name = "Typescript"
print(f"{age} is of type {type(age)}")
print(f"{course_rating} is of type {type(course_rating)}")
print(f"{course_name} is of type {type(course_name)}")

# Exercise 5 — Concatenating Strings
instructor = "Oluwaseyi"
academy_name = "AfricaPlan"
slogan = "Learning python is fun!"
print(f"The instructor, {instructor} at {academy_name} says: '{slogan}'.")

# Part B — Data Types & Conversions
# Exercise 6 — Convert String to Integer and Vice Versa
string_number = "100"
integer_number = 42
print(f"Integer Value: {string_number}, Type: {type(int(string_number))} ")
print(f"String Value: {integer_number}, Type: {type(str(integer_number))} ")

# Exercise 7 — Convert Float to Integer and Vice Versa
float_number = 9.75
integer_number = 50
print(f"Float to Int: {int(float_number)}, Type: {type(int(float_number))}")
print(f"Int to Float: {float(integer_number)}, Type: {type(float(integer_number))}")

# Exercise 8 — Convert a Boolean to an Integer
true_value = int(True)
false_value = int(False)
print(f"True as an integer: {true_value}")
print(f"False as an integer: {false_value}")

# Exercise 9 — Convert List to a String and Back
text_list = ['Python', 'is', 'amazing']
new_text = ", ".join(text_list)
new_list = new_text.split(", ")
print(f"List to string: {new_text}")
print(f"String to List: {new_list}")

# Exercise 10 — Convert Dictionary Keys and Values to Lists
academy = {
    "name": "Lkhibra Academy",
    "age": 5,
    "language": "Python"
}
keys = list(academy.keys())
values = list(academy.values())
print(f"Keys: {keys}")
print(f"Values: {values}")

# Part C — Operators & Expressions
# Exercise 11 — Perform Arithmetic Operations
add = 10+5
sub = 10-5
mult = 10*5
div = 5/2
modu = 10%5
print(f"Addition: {add}")
print(f"Subtration: {sub}")
print(f"Multiplication: {mult}")
print(f"Division: {div}")
print(f"Modulus: {modu}")

# Exercise 12 — Use Comparison Operators
a_int = 10
b_int = 5
print(f"10 > 5: {a_int > b_int}")
print(f"10 < 5: {a_int < b_int}")
print(f"10 == 10: {a_int == a_int}")
print(f"10 != 5: {a_int != b_int}")
print(f"10 >= 5: {a_int >= b_int}")
print(f"10 <= 5: {a_int <= b_int}")

# Exercise 13 — Use Logical Operators
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"Not True: {not True}")

# Exercise 14 — Use Assignment Operators
q = 10
q += 5
print(f"After += : {q}")
q -= 3
print(f"After -= : {q}")
q *= 2
print(f"After *= : {q}")
q /= 3
print(f"After /= : {q}")
q %= 2
print(f"After %= : {q}")

# Exercise 15 — Use Bitwise Operators
print (f"5 & 3 = {5 & 3}")
print(f"5 | 3 = {5 | 3}")
print(f"5 ^ 3 = {5 ^ 3}")
print(f"5 << 1 = {5 << 1}")
print(f"5 >> 1 = {5 >> 1}")

# Part D — Conditionals
# Exercise 16 — Check if a Number is Even or Odd
new_num = int(input("Enter a number: "))
if new_num % 2 == 0:
    print(f"{new_num} is an even number")
else:
    print(f"{new_num} is an odd number")

  # Exercise 17 — Find the Largest Number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}.")

# Exercise 18 — Check if a Year is a Leap Year
year = int(input("Enter a year: "))
if year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Exercise 19 — Grade Classifier
test_score = int(input("Enter your test score: "))
if test_score >= 90:
    grade = "A"
elif test_score >= 80:
    grade = "B"
elif test_score >= 70:
    grade = "C"
elif test_score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {test_score} -> Grade: {grade} ")

# Part E — String Operations & Formatting
# Exercise 20 — Extract the Domain from an Email
address = "kosikaira565@gmail.com"
new_add = address.split("@")
print(f"Domain: {new_add[1]}")

# Exercise 21 — Count the Occurrences of a Word in a Review
review = input("Enter your review: ")
count = review.lower().count("quality")
print(f"The word 'quality' appears {count} time(s).")

# Exercise 22 — Format an Invoice
CARD_WIDTH = 20
item1 = "Laptop"
item2 = "Mouse"
lap_price = 1200.99
mou_price = 25.50
print('-' * 3)
print("Item         Price")
print("-" * CARD_WIDTH)
print(f"{item1 : <10}     ${lap_price}")
print(f"{item2 : <10}     ${mou_price}")
print('-'* 3)

# Exercise 23 — Reverse Words in a Sentence
sentence = "Lkhibra Academy is great"
words = sentence.split()
reversed_words = words[::-1]
result = " ".join(reversed_words)
print(result)

# Exercise 24 — Extract Hashtags from a Social Media Post
import re
text = "Loving #Python and #Coding at #LkhibraAcademy"
hashtags = re.findall(r"#\w+", text)
print(f"Hashtags: {hashtags}")

# Exercise 25 — Validate a Password Strength
password = input("Enter your password: ")
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)
if len(password) >= 8 and has_number and has_special:
    print("Password is valid")
else:
    print("Password is invalid")

## Exercise 26 — Remove Extra Spaces from a String
text = " Hello   World  !  "
clean_text = " ".join(text.split())
print(clean_text)

# Exercise 27 — Convert a String to Title Case
text = "lkhibra academy python training"
title_text = text.title()
print(title_text)

# Exercise 28 — Replace Words in a Text
text = "I love Python programming"
text = text.replace("Python", "Java")
print(text)

# Exercise 29 — Check How a String Starts or Ends
filename = input("Enter a filename: ")
if filename.lower().startswith("report") and filename.lower().endswith(".pdf"):
    print("This is a valid report PDF file.")
else:
    print("Invalid file format")

