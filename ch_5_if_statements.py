# 5-1 conditional tests
# 5-2 more conditional tests

message = 'hello'
if message == 'hi':
    print("the message is : 'hi' ")
else:
    print("the message is not 'hi'")

message = 'HELLO'
message = message.lower()
if message == 'hello':
    print("the message is 'hello'")

x = 5
y = 99
if x == y:
    print("x is equal to y")
if x > y:
    print("x is greater than y")
if x < y:
    print("x is less than y")

z = 55
if x < y and y > z:
    print("both conditions are true")

if x > y or y > z:
    print('at least one condition is true')

items = ['item1', 'item2', 'item3', 'item4']
if 'item3' in items:
    print('item3 exists in item list')

if 'item33' not in items:
    print('item33 is not in the items list')

# 5-3 alien colors 1
alien_color = 'green'
if alien_color == 'green':
    print('you have earned 5 points')

alien_color = 'yellow'
if alien_color == 'green':
    print('you have earned 5 points')

# 5-4 alien colors 2
if alien_color == 'green':
    print('yes, u guessed right !')
else:
    print("ooh, you didn't guess it right ")

# 5-5 alien colors 3
if alien_color == 'green':
    print('u earned 5 points')
elif alien_color == 'red':
    print('u earned 10 points')
else:
    print('u earned 15 points')

# 5-6 stages of life

age = 24

if age < 2:
    print('you are a baby yet')
elif age == 2 or age < 4:
    print('you are a toddler :)')
elif age == 4 or age < 13:
    print('you are a kid ')
elif age == 13 or age < 20:
    print('you are a teenager')
elif age == 20 or age < 65:
    print('you are an adult')
elif age > 65:
    print('you are an elder')

# 5-7 favorite fruit

favorite_fruit = ['strawberry', 'apple', 'blueberry', 'banana', 'clementine']
if 'apple' in favorite_fruit:
    print('yes, you like apple')
if 'lemon' in favorite_fruit:
    print('yes, you like lemon')
if 'banana' in favorite_fruit:
    print('yes, you like banana')
if 'mango' in favorite_fruit:
    print('yes, you like mango')
if 'strawberry' in favorite_fruit:
    print('yes, you like strawberry')

# 5-8 hello admin
usernames = ['admin', 'eric', 'mark', 'jane', 'adams']
for username in usernames:
    if username == 'admin':
        print('hello admin, would u like to see a status report ? ')
    else:
        print('hello ' + username + ', thank you for logging in again.')

# 5-9 no users

while len(usernames) != 0:
    usernames.remove(usernames[0])
    users = usernames[:]
    if not users:
        print('we need to find some users!')

# 5-10 checking usernames
current_users = ['admin', 'eric', 'mark', 'jane', 'adams']
new_users = ['JANE', 'mike', 'alex', 'Mark', 'jenny']

for value in new_users:
    if value.title() and value.upper() and value.lower() in current_users:
        print('this username is not available')
    else:
        print('username is available')


# 5-11 ordinal numbers
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(str(1) + 'st', end=' ')
    elif number == 2:
        print(str(2) + 'nd', end=' ')
    elif number == 3:
        print(str(3) + 'rd', end=' ')
    else:
        print(str(number)+'th', end=' ')

