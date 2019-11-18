formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4)) # there are 4 arguments here that fill in the {}
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format( # look closely, there are still 4 arguments here that need love and attention
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
))