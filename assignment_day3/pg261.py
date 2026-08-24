"""
Make a list containing a series of short text messages. Pass
the list to a function called show_messages(), which prints each text message.
"""
# def show_messages(messages):
#     for message in messages:
#         # print(message)

# messages = [
#     "Hello!",
#     "How are you?",
#     "See you later.",
#     "Have a great day!"
# ]

# show_messages(messages)

"""
Start with a copy of your program from Exercise
8-9. Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""
def send_messages(messages):
    sent_messages = []

    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
        return sent_messages


messages = [
    "Hello!",
    "How are you?",
    "See you later.",
    "Have a great day!"
]

sent_messages = send_messages(messages)

print("\nOriginal list:")
print(messages)

print("\nSent messages:")
print(sent_messages)


"""
Start with your work from Exercise 8-10. Call
the function send_messages() with a copy of the list of messages. After calling
the function, print both of your lists to show that the original list has
retained its messages.
"""

sent_messages = send_messages(messages[:])

print("\nOriginal list:")
print(messages)

print("\nSent messages:")
print(sent_messages)