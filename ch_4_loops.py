# 4-1
pizzas = ['margherita', 'pepperoni', 'mexican']
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("I like " + pizza + ".")


# 4-2 animals

animals = ['cat', 'dog', 'bird']
for animal in animals:
    print(animal)
for animal in animals:
    print("A " + animal + " would make a great pet")
print("\n Any of these animals would make a great pet")

# 4-3 counting to twenty
for value in range(1, 21):
    print(value, end=" ")
print("\n")

# 4-4 one million
# for value in range(1, 1000001):
#       print(value)


# 4-5 summing a million
a_million = []
for value in range(1, 1000001):
    a_million.append(value)
print(min(a_million))
print(max(a_million))
print(sum(a_million))

# 4-6 odd numbers
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number, end=" ")
print("\n")

# 4-7 threes
threes = list(range(3, 31, 3))
for number in threes:
    print(number, end=" ")
print("\n")

# 4-8 cubes
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes, end=" ")
print("\n")

# 4-9 cube comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes, end=" ")
print("\n")


# 4-10  slices
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("the first three items in the list are : " + str(list_1[:3]))
print("three items from the middle of the list are: " + str(list_1[3:6]))
print("the last three items in the list are : " + str(list_1[6:]))

# 4-11 my pizzas, your pizzas
friend_pizzas = pizzas[:]
pizzas.append("italian")
friend_pizzas.append("vegetarian")
print("my favourite pizzas are: " + str(pizzas))
print("my friend's favourite pizzas are: " + str(friend_pizzas))

# 4-12 more loops
foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
# didn't get

# 4-13 buffet
basic_foods = ('soup', 'chicken crispy', 'pizza', 'fried_potato', 'falafel')
for food in basic_foods:
    print(food)
print("\n new tuple \n")

basic_foods = ('spaghetti', 'pasta', 'pizza', 'fried_potato', 'falafel')
for food in basic_foods:
    print(food)