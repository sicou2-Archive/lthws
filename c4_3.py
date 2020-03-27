#Counting to 20
for x in range(21):
	print(x)

#4-4 One Million 

million = list(range(1_000_001))

for num in million:
#	print(num)
    pass
#4-5 Summin a million 

min_mil = min(million)
max_mil = max(million)
print('min = ' + str(min_mil) + ' ' + 'max = ' + str(max_mil))

sum_mil = sum(million)
print(sum_mil)

#4-6 Odd numbers 
odd_num = list(range(1,21,2))
for num in odd_num:
	print(num)

#4-7 Threes
threes = list(range(3,31,3))
for num in threes:
	print(num)

#4-8 Cubes and accidentally 4-9
#numbers = list(range(1,11))
#for num in numbers:
numbers = [num ** 3 for num in range(1,11)]

print(numbers)