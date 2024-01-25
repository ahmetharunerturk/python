import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_int=random.randint(0,len(names))

print(f"{names[random_int]} is going to buy the meal today!")