# 3-1.Names

names = ['Jane', 'Anne', 'Beatrice']
print(names[0])
print(names[1])
print(names[2])

# 3-2.greetings:
message = "Hello, "
print(message+names[0])
print(message+names[1])
print(message+names[2])

# 3-3.your own list

# 3-4.guest list

guests = ["grandma", "aunt", "niece", "cousin"]
print("Dear " + guests[0].title() + ", here I'm inviting u for a dinner tonight!")
print("Dear " + guests[1].title() + ", here I'm inviting u for a dinner tonight!")
print("Dear " + guests[2].title() + ", here I'm inviting u for a dinner tonight!")
print("Dear " + guests[3].title() + ", here I'm inviting u for a dinner tonight!" + "\n")

# 3-5.changing guest list
print(guests[3].title() + " cannot come !")

guests[3] = "new_friend"

print("Dear " + guests[0].title() + ", here I'm inviting u for a dinner tonight!")
print("Dear " + guests[1].title() + ", here I'm inviting u for a dinner tonight!")
print("Dear " + guests[2].title() + ", here I'm inviting u for a dinner tonight!")
print("Dear " + guests[3].title() + ", here I'm inviting u for a dinner tonight!" + "\n")


# 3-6. more guests
print("good news... found a bigger dinner table" + "\n")
guests.insert(0, "emily")
guests.insert(2, "anna")
guests.append("tommy")

for invited_guests in guests:
    print("Dear " + invited_guests.title() + ", here I'm inviting u for a dinner tonight!")

# 3-7 shrinking your guest list

print("\n dinner table won't come on time, i can invite only 2 people \n")
print(guests)

guests = ['emily', 'grandma', 'anna', 'aunt', 'niece', 'new_friend', 'tommy']
while len(guests) != 2:
    popped_guest = guests.pop(0)
    final_list = guests[:]
    print("sorry " + popped_guest + " I cant invite u for the dinner")

print('\n final guest list is :' + str(guests) + '\n')
# 3-8 seeing the world

locations = ["norway", "denmark", "canada", "indonesia", "japan"]
print(locations)
print(sorted(locations))

print(locations)
print(sorted(locations, reverse=True))

print(locations)
locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

# 3-9 number of people invited to dinner// results are not correct
print(len(popped_guest), len(guests))

# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
# Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.
# DIDN'T GET IT
