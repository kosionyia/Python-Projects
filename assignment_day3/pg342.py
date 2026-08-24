"""
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to
convert the input to an int, you’ll get a ValueError. Write a program that
prompts for two numbers. Add them together and print the result. Catch the
ValueError if either input value is not a number, and print a friendly error
message. Test your program by entering two numbers and then by entering
some text instead of a number.
"""
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 + num2

    print(f"The answer is {result}.")

except ValueError:
    print("Sorry, please enter numbers only.")


"""
code from 10-5
Write a while loop that prompts users for their name.
Collect all the names that are entered, and then write these names to a file
called guest_book.txt. Make sure each entry appears on a new line in the
file.
"""
names = []

while True:
    name = input("Enter your name (or 'q' to quit): ")

    if name == "q":
        break

    names.append(name)

with open("guest_book.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

"""
ex 10-7
Wrap your code from Exercise 10-5 in a while
loop so the user can continue entering numbers, even if they make a
mistake and enter text instead of a number.
"""
while True:
    name = input("Enter your name (or 'q' to quit): ")

    if name == "q":
        break

    try:
        number = int(input("Enter a number: "))
        print(f"Hello {name}, you entered {number}.")

    except ValueError:
        print("Please enter a valid number.")

"""
Make two files, cats.txt and dogs.txt. Store at least
three names of cats in the first file and three names of dogs in the second
file. Write a program that tries to read these files and print the contents of
the file to the screen. Wrap your code in a try-except block to catch the
FileNotFound error, and print a friendly message if a file is missing. Move one
of the files to a different location on your system, and make sure the code in
the except block executes properly.
"""
files = ["cats.txt", "dogs.txt"]

for filename in files:
    # try:
    #     with open(filename) as file:
    #         contents = file.read()

    #     print(f"\nContents of {filename}:")
    #     print(contents)

    # except FileNotFoundError:
    #     print(f"\nSorry, the file {filename} was not found.")

    """
Modify your except block in Exercise 10-7 to
fail silently if either file is missing.
"""
    try:
        with open(filename) as file:
            contents = file.read()

        print(f"\nContents of {filename}:")
        print(contents)

    except FileNotFoundError:
        pass


"""
Visit Project Gutenberg (https://gutenberg.org)
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the
number of times 'row' appears in a string:
 >> line = "Row, row, row your boat"
>> line.count('row')
2
>> line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches all
appearances of the word you’re looking for, regardless of how it’s formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text. This will be
an approximation because it will also count words such as 'then' and 'there'.
Try counting 'the ', with a space in the string, and see how much lower your
count is.
"""
files = ["book1.txt", "book2.txt", "book3.txt"]

for filename in files:
    try:
        with open(filename) as file:
            contents = file.read()

        the_count = contents.lower().count("the")
        the_space_count = contents.lower().count("the ")

        print(f"\n{filename}")
        print(f"'the' appears approximately {the_count} times.")
        print(f"'the ' appears approximately {the_space_count} times.")

    except FileNotFoundError:
        pass
