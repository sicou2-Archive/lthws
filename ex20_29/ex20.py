from sys import argv # importing argv from sys

script, input_file = argv # sets variable names to things passes from the command line 

def print_all(f): # def print_all method with f variable
    print(f.read()) # prints the whole file with read 

def rewind(f): # defs rewind method with vaiable f
    f.seek(0) # moves read head to 0 bit in the file

def print_a_line(line_count, f): # defs print a line with 2 variables
    print(line_count, f.readline(), end = "") # prints the passed line number from the variable, and reads the current assigned line from the file
    
current_file = open(input_file) # opens the command line input_file and sets it to current_file

print("First let's print the whole file:\n")

print_all(current_file) # calls function print_all with variable current_file

print("\nNow let's be kind, and rewind! Kind of like a tape.")

rewind(current_file) # runs rewind function on current_file

print("Let's print three lines:")

current_line = 1 # sets current line to 1
print_a_line(current_line, current_file) # runs print_a_line method with passed variables

current_line += 1 # increments line by one
print_a_line(current_line, current_file)

current_line += 1  
print_a_line(current_line, current_file)