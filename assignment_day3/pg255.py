"""
Write a function called city_country() that takes in the
name of a city and its country. The function should return a string formatted
like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""

def city_country(city, country):
    return f"{city}, {country}"

# print(city_country("santiago", "Chile"))
# print(city_country("Lagos", "Nigeria"))
# print(city_country("London", "England"))

"""
Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing
different albums. Print each return value to show that the dictionaries are
storing the album information correctly.
"""

# def make_album(artist, title):
#     album = {
#         "artist": artist,
#         "title": title 
#         }
#     return album

# album1 = make_album("Davido", "Timeless")
# album2 = make_album("Burna Boy", "Love, Damini")
# album3 = make_album("Wizkid", "Made in Lagos")

# print(album1)
# print(album2)
# print(album3)

"""
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value
for the number of songs, add that value to the album’s dictionary. Make at
least one new function call that includes the number of songs on an album.
"""
def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs:
        album["songs"] = songs

    return album


album1 = make_album("Davido", "Timeless")
album2 = make_album("Burna Boy", "Love, Damini")
album3 = make_album("Wizkid", "Made in Lagos", 14)

print(album1)
print(album2)
print(album3)

"""
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have
that information, call make_album() with the user’s input and print the
dictionary that’s created. Be sure to include a quit value in the while loop.
"""
while True:
    print("\nEnter your favorite album information.")
    print("Enter 'q' at any time to quit.")

    artist = input("Artist name: ")

    if artist == "q":
        break

    title = input("Album title: ")

    if title == "q":
        break
    
    album = make_album(artist, title)

    print(album)