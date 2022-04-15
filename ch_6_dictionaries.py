# 6-1 person

ef_housley = {'first_name': 'effie',
              'last_name': 'housley',
              'age': '19',
              'city': 'vancouver'}
print(ef_housley)

# 6-2 favorite numbers
favorite_number = {'sam': '6',
                   'jack': '4',
                   'maia': '7',
                   'elvin': '9'}
print(favorite_number)

# 6-3 glossary -> skipping this
# 6-4 glossary 2
words = {
    'mumble': 'to speak quietly',
    'intrigue': 'to interest someone a lot',
    'indigent': 'very poor',
    'prominent': 'very well known',
    'loudhailer': 'megaphone'}
for key, value in words.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

# 6-5 rivers
rivers = {
    'nile': 'egypt',
    'colorado': 'USA',
    'dnieper': 'russia',
    'don': 'russia'}
for key, value in rivers.items():
    print('the ' + key + ' runs through ' + value)

for key, value in rivers.items():
    print(key, end=' ')
print('\n')

for key, value in rivers.items():
    print(value, end=' ')
print('\n')

# 6-6 polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', }

for_poll = ['jen', 'anne', 'vilson', 'sarah', 'edward', 'mark']
for people in for_poll:
    if people in favorite_languages:
        print(people + ' thank you for taking poll')
    else:
        print(people + ' we invite you to take the poll')


# 6-7 people
# 6-8 pets
# 6-9 favorite places
# 6-10 favorite numbers
# 6-11 cities
cities = {
    'cluj-napoca': ' -> romania, 308.000, the heart of transilvania',
    'krakow': ' -> poland, 760.000, city has its own anthem',
    'stockholm': ' -> sweden, 975.000, one of the world\'s cleanest metropolises'
}
for key, value in cities.items():
    print(key + value)


# 6-12 extensions -> skipping


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

print(aliens[0]['color'])
