name = 'Brayton C. Lee'
age = 32
height = 73
cm_height = round((height * 2.54),2)
weight = 170
kg_mass = round((170 / 2.205),2)
eyes = 'brown'
teeth = 'white'
hair = 'blond'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall. That is {cm_height} in centemeters")
print(f"He's {weight} pounds heavy. That is {kg_mass} kilograms")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right

total = age + height + weight
print(f"If I add my age of {age}, my height of {height}, and my weight of {weight}, I get a total of {total}.")