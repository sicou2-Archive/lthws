from sys import argv
from os.path import exists

script, from_file, to_file, = argv

print(f"Copying from {from_file} to {to_file}.")

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read() 
# trying to do it on one line/ on one line indata is a string and 
#apparently does not need to be closed

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit ENTER to continue, CTRL-C to abort.") 
# apparently it is annoying to have a confirmation step told to take it out

# input()

# out_file = open(to_file, 'w').write(indata) 
#lets experiment with this to one line 
#.write returns the number of bytes actually written hence 'int'

# out_file.write(indata)

out_file = open(to_file, 'w').write(indata) 
# another one line experiment might not need to close this either

print("Alright, all done!")

# out_file.close() # this variable is a '_io.TextIOWeapper' and should be closed 
#no longer needed due to 'operation one line two the electric linealoo

# in_file.close() # this became indat / this variable no longer exists
# indata.close()  # this variable is a string and does not need to be closed