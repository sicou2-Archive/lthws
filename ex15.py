from sys import argv # from sys import argv method

script, filename = argv # sets the command line arguments to variables

txt = open(filename) # creates variable txt that opens "filename"

print(f"Here's your file {filename}:") # format prints a sentence and the variable filename
print(txt.read()) # prints txt using the read command /might want to look in to how open works some more/ also maybe read

print("Type the filename again:") # print function
file_again = input("> ") # variable "file_again" looking for another file to open and read

txt_again = open(file_again) # "txt_again" to open the previous new file

print(txt_again.read()) # use read to read this new opened file

txt.close() # these close the opened file
txt_again.close()