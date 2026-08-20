word = input("Enter a word or phrase")
new_word = word.strip().lower()
if new_word == new_word[::-1]:
    print(f"{new_word} is a palindrome")
else:
    print(f"{new_word} is not a palindrome")