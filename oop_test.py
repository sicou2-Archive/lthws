import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = { # dict of phrases to be used
    "class %%%(%%%):": # the %%% will be replaces later in convert()
      "Make a class names %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.", 
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# Do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    # this is looking to see if the cmd prompt has 1 or 2 args
    
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
    
# Load up the words from the website
for word in urlopen(WORD_URL).readlines(): 
    # here we are loopoing through the 'urlopen' with the site given
    # to WORD_URL by each line via .readlines()
    WORDS.append(str(word.strip(), encoding="utf-8"))
    # with this we are taking each 'word line' stripping the white space
    # ensuring that the encoding is utf-8 and then turning it in to a 
    # string, from there that str 'word' is being appended to the empty
    # but not for long list of WORDS (a global variable)
    
def convert(snippet, phrase): 
    # convert takes two arguments 
    class_names = [w.capitalize() for w in 
                   random.sample(WORDS, snippet.count("%%%"))]
                   # *THIS* is a List Comprehension something he says 
                # nothing of. 
            # w will be capitalized for w in a random sample of 
        # words from the population from WORDS and the number of things
    # to be selected is the snipper.count of the number of "%%%" in the 
    # string that is passed to it later from the 'try' below
    other_names = random.sample(WORDS, snippet.count("***"))
    # this is the same thing except we do not need to cap the words and
    # it is looking for "***"
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
    # Looking up count, I think I understand what the purpose of the 
    # method is, however, I *DO NOT* understand exactly what 
    # non-overlapping mean and and utterly failing with my Google search
    # Here we are itterating over i in the range of 0 to the number of 
    # times that "@@@" appears in the snippet
        param_count = random.randint(1, 3)
        param_names.append(', '.join(
    # so .join is a thing that was used in ex38 to stick things together
    # seperated by the first arg in the method. In this cast it is ', '
            random.sample(WORDS, param_count)))
    # this is setting up a random number of parameters that will be 
    # in the lists later, from 1 to 3
        
    for sentence in snippet, phrase: # this looks like it is iterating 
        # over each k-v pair. 
        ########STOPPED HERE TRYING TO FIGURE OUT THIS DOUBLE LOOP AND 
        ####### EXACTLY WHERE EVERYTHING IS COMING FROM 
        result = sentence[:]
        
        # Fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        
        # Fake other names   
        for word in other_names:
            result = result.replace("***", word, 1)
            
        # Fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
            
        results.append(result)
        
    return results
    
    
# Keep going until they hit CTRL-D #ZED HAS D HERE I NEED Z
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        
        for snippet in snippets: # snippet here is the key 
            phrase = PHRASES[snippet] # phrase is the value
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
                
            print(question)
            
            input("> ")
            print(f"ANSWER:  {answer}\n\n")
except EOFError:
    print("\nBye")
        