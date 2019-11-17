types_of_people = 10 # sets a variable to 10
x = f"There are {types_of_people} types of people." # sets a variable to a formatted string 

binary = "binary" # sets a variable to a string
do_not = "don't" # diddo
y = f"Those who know {binary} and those who {do_not}." # sets a variable with a formatted string

print(x) # prints a variable
print(y) # diddo

print(f"I said: {x}") # prints a formatted string with a variable call
print(f"I also said: '{y}'") # diddo

hilarious = False # sets a variable to a boolian values
joke_evaluation = "Isn't that joke so funny?! {}" # sets a veriable to a string with a spot for another variable to be called

print(joke_evaluation.format(hilarious)) # prints the variable joke_evaluation formatted with the variable hilarious # it looks like when calling .format you have to have the variable it needs to be called

print(joke_evaluation) # however if you do not put the .format in there then it will just print the {} 

w = "This is the left side of ..." # sets a variable with a string
e = "a string with a right side." # diddo

print(w + e) # concatinates two variables together to be printed