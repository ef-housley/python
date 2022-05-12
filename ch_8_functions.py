# 8-1. Message:
# Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.

def display_message():
    print("I am learning about functions")


display_message()


# 8-2. Favorite Book:
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as One of my favorite books is Alice in Wonderland.
# Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    print("my favorite book is " + title)


favorite_book("Alice in the wonderland")


# 8-3 T-Shirt:
# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

def make_shirt(size, text):
    print("the t-shirt size = " + size + " and the text = " + text)


make_shirt("34", "limited edition")
make_shirt(size="s", text="smile")


# 8-4 Large Shirts:
# Modify the make_shirt() function so that shirts are large by default
# with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with
#  a different message.

def make_shirt(size='large', text='I love python'):
    print("the t-shirt size = " + size + " and the text = " + text)


make_shirt()
make_shirt('medium')
make_shirt('small', 'a different message')


# 8-5 Cities:
# Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavík is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is
# not in the default country

def describe_city(name, country='Poland'):
    print(name + " is in " + country)


describe_city('olsztyn')
describe_city('lodz')
describe_city('stockholm', 'sweden')


# 8-6 City Names:
#  Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned

def city_country(city, country):
    value = city + ', ' + country
    return value.title()


new_city_country = city_country("amsterdam", "netherlands")
print(new_city_country)
new_city_country = city_country("copenhagen", "denmark")
print(new_city_country)
new_city_country = city_country("helsinki", "finland")
print(new_city_country)


# 8-7. Album
#  Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the
# number of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.


def make_album(artist, album, tracks=" "):
    music_album = {'artist': artist, 'album': album}
    if tracks:
        music_album['tracks'] = tracks
    return music_album


new_album = make_album('lucas graham', '7 years old')
print(new_album)
new_album = make_album('adele', 'set fire to the rain')
print(new_album)
new_album = make_album('ed sheeran', '=')
print(new_album)

new_album = make_album('billie eilish', 'ocean eyes', '4')
print(new_album)

# 8-8. User Albums:
# Start with your program from Exercise 8-7. Write a 'while'
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

while True:
    print("enter q anytime to quit ")

    artist_name = input(" artist's name: ")
    if artist_name == "q":
        break
    album_title = input("album title: ")
    if album_title == "q":
        break

    new_album = make_album(artist_name, album_title)
    print(new_album)

# 8-9 Magicians:
# Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list

magician_names = ["Apollo", "Blaine", "Copperfield", "Derren", "Devant"]


def show_magicians(magicians):
    for magician in magicians:
        msg = "hello, " + magician + "!"
        print(msg)


show_magicians(magician_names[:])


# 8-10 Great Magicians:
# Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians
# by adding the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.


def make_great(magician_names_edited, new_magician):
    while magician_names_edited:
        magician = "Great " + magician_names_edited.pop()
        new_magician.append(magician)


new_list_magician = []
# make_great(magician_names, new_list_magician)

print(magician_names[:])
show_magicians(new_list_magician[:])

# 8-11. Unchanged Magicians:
#  Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.

make_great(magician_names[:], new_list_magician)
show_magicians(magician_names[:])
show_magicians(new_list_magician[:])


# 8-12.Sandwiches:
# Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the
# sandwich that is being ordered. Call the function three times, using a different
# number of arguments each time.

def make_sandwiches(*extra):
    print("make a sandwich with: " + str(extra))


make_sandwiches("cheese")
make_sandwiches("cheese", "tomatoes", "fried potatoes")
make_sandwiches("steak", "red cabbage", "cucumber", "onion")


# 8-13. User Profile:
#  Start with a copy of user_profile.py from page 153. Build
# a profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('effie', 'housley',
                             location='canada',
                             field='geography',
                             age='56')
print(user_profile)


# 8-14. Cars:
# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def build_car(manufacturer, model_name, **other_info):
    car = {'manufacturer': manufacturer, 'model': model_name}
    for key, value in other_info.items():
        car[key] = value
    return car


new_car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(new_car)

# 8-15 Printing models: --> skipping
# Put the functions for the example print_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of print_models.py, and modify the file to use the imported functions.


# 8-16 Imports --> skipping
# 8-17 styling functions --> skipping

