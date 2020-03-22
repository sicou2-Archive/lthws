import ex25 #With import you must include "ex25." before any method you are trying to call

def main():
    sentence = "All good things come to those who wait."
    words = ex25.break_words(sentence)
    print(words)
    sorted_words = ex25.sort_words(words)
    print(sorted_words)
    ex25.print_first_word(sorted_words)
    ex25.print_last_word(sorted_words)
    print(sorted_words)
    sorted_words = ex25.sort_sentence(sentence)
    print(sorted_words)
    ex25.print_first_and_last(sentence)
    ex25.print_first_and_last_sorted(sentence)
    
main()


from ex25 import * #With from it seems like you do not need to inlude "ex25." before the method else you will get an error since ex25 is not defined in the ex25 module

def apple():
    sentence = "I want to beleive as many true things and as few false things as possible."
    words = break_words(sentence)
    print(words)
    sorted_words = sort_words(words)
    print(sorted_words)
    print_first_word(sorted_words)
    print_last_word(sorted_words)
    print(sorted_words)
    sorted_words = sort_sentence(sentence)
    print(sorted_words)
    print_first_and_last(sentence)
    print_first_and_last_sorted(sentence)    

apple()
