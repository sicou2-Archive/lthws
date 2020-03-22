import sys #import sys as a whole
script, input_encoding, error = sys.argv #set script.py, the input encoding (utf-8), and the error reporting method (strict) to argv from sys


def main(language_file, encoding, errors): #def main using later "languages" variable, and the cml variables input_encoding and error
    line = language_file.readline() #read the line and set to line, if EOF and no \n, returns partially read data, if that buffer is empty it returns an empty bytes object, this should be a null allowing "if line" below to be false
    if line: #if line is true
        print_line(line, encoding, errors) #run the print line method defined below
        return main(language_file, encoding, errors) # return main,since it is apart of the if, it will not loop forever, however it will loop



def print_line(line, encoding, errors): # def print_line method called above with 3 args, line (from above), encoding (from cml), and errors (from cml)
    next_lang = line.strip()  #with no args only white space is removed from the line, also, apparently the \n is stripped as well #the current called line is striped and set to next_lang
    raw_bytes = next_lang.encode(encoding, errors=errors) # encode method with encoding from input_encoding and errors from error # I wonder if I can use next_lang.encode(encoding, errors) #it looks like I looked up the wrong encode maybe should have used CodecInfo instead of codec method
    cooked_string = raw_bytes.decode(encoding, errors=errors) #this is the second half of the to be printed string below where we are decoding the above encoded string

    print(raw_bytes, "<===>", cooked_string) # print, nothing new


languages = open("languages.txt", encoding="utf-8") #setting the file to be used and the encoding 

main(languages, input_encoding, error) #runs main using established args from above

###### Am skipping the Breaking it portion of this exercise- the broken everything that is utf-8 with these consoles is making this super difficult and I just want to move on. 