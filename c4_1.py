#Pizzas

pizzas = ["bacon", "ham", "pineapple"]

for pizza in pizzas:
	print(f"I enjoy {pizza} pizza.")

print("All different kinds of pizza is tasty!")

friend_pizzas = pizzas[:]
pizzas.append("sausage")
friend_pizzas.append("cheese")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)