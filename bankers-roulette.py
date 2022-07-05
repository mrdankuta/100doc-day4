import random

# randomInteger = random.randint(1, 10)
# print(randomInteger)


names_string = input("Give me everybody's names, separated by a comma. \n")

names = names_string.split(", ")

number_of_names = len(names)

randomNameIndex = random.randint(0, number_of_names - 1)

payer = names[randomNameIndex]

print(payer + " will pay for everyone.")
