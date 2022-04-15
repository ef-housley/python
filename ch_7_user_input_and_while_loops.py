# 7-1 rental car
message = input("welcome, what kind of rental car would you like ?\n ")
print("let me see if I can find " + message + " car for you...")

# 7-2 restaurant seating
question = int(input('how many people are there in your dinner group\n'))
if question > 8:
    print('you will have to wait for a table')
else:
    print('your table is ready !')

# 7-3 multiples of ten
number = int(input('please introduce a number: \n'))
if number % 10 == 0:
    print('your number is a multiple of 10')
else:
    print('your number is not a multiple of 10')

# 7-4 pizza toppings
pizza_toppings = input("please enter your preferred toppings for pizza: \n")
while pizza_toppings != 'quit':
    print(pizza_toppings + ' will be added to your pizza.\n '
                            'what else would you like to add ?')
    pizza_toppings = input()

# 7-5 movie tickets
age = int(input(' (type 0 to quit )\n'
                'how old are you? \n'))
while age != 0:

    if age < 3:
        print('your movie ticket is free')
    elif age <= 12:
        print('your movie ticket is $10')
    else:
        print('your ticket is $15')

    age = int(input('how old are you? \n'))

# 7-6 three exits
active = True
while active:
    message = str(input('what is your favourite city ? \n'))
    if message == "quit":
        break
    else:
        print(message + ' is a great city')


# 7-7 infinity
# 7-8 deli
sandwich_orders = ['pastrami sandwich',
                   'tuna sandwich',
                   'egg sandwich',
                   'fish sandwich',
                   'bacon sandwich']
finished_sandwiches = []
while sandwich_orders:
    finished = sandwich_orders.pop(0)
    print(' your ' + finished + ' is ready')
    finished_sandwiches.append(finished)

print('all sandwich orders are done: ' + str(finished_sandwiches))


# 7-9 no pastrami
no_pastrami = ['pastrami',
                'tuna sandwich',
                'egg sandwich',
                'pastrami',
                'fish sandwich',
                'pastrami',
                'bacon sandwich']

finished_sandwich = []

print('deli has run out of pastrami')

while 'pastrami' in no_pastrami:
    no_pastrami.remove('pastrami')

while no_pastrami:
    finished = no_pastrami.pop(0)
    print(' your ' + finished + ' is ready')
    finished_sandwich.append(finished)

print('all sandwich orders are done: ' + str(finished_sandwich))


# 7-10 dream vacation

answers = {}

poll_active = True
while poll_active:
    name = input(' what is your name ?\n')
    answer = input('If you could visit one place in the world,where would you go? \n')

    answers[name] = answer

    repeat = input('anybody else willing to answer ? (yes/no) \n')
    if repeat == 'no':
        poll_active = False

print('\n------->results<----------')
print(name + ' wants to visit ' + answer + '.')