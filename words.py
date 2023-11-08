def print_upper_words(words, must_start_with=["e"]):
    """Put in a list of words and only print out the words that start with certain letters in uppercase"""
    for word in words:
        for first in must_start_with:
            if word.find(first.upper()) == 0 or word.find(first.lower()) == 0:
                print(word.upper())


print_upper_words(["eagle", "Edward", "Alfred"])
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
print_upper_words(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])
