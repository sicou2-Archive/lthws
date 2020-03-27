for value in range(1,5):
	print(value)

for value in range(5):
	print(value)

numbers = list(range(1,6))
print(numbers)

#even_numbers

even_numbers = list(range(2,11,2))
print(even_numbers)

#squares.py
squares = []
for value in range(1,11):
	# square = value ** 2
	# squares.append(square)
	# A better way to do this
	squares.append(value ** 2)

print(squares)

digits = list(range(0,10))
print(digits)
minimum = min(digits)
print(minimum)
maximum = max(digits)
print(maximum)
summation = sum(digits)
print(summation)

#squares, except this time with list comprehension

#A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
#The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
squares = [value ** 2 for value in range(1,25)]
print(squares)

