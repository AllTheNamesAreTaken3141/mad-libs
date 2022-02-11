"""Its mad libs"""

file = open("source.txt", "r")
source = file.read()

def locate_blanks(source):
    """Searches through the source string and locates the blanks where words will be added."""

    words = []
    current_word = ""
    currently_adding = False

    for i in source:
        if i == "<":
            currently_adding = True
            continue
        if i == ">":
            currently_adding = False
            words.append(current_word)
            current_word = ""
        if currently_adding:
            current_word += i

    if current_word != "":
        words.append(current_word)

    return words

def get_words(blanks):
    """Gets a word from the user to fill in every blank"""
    
    words = []

    for i in blanks:
        if i[0] in "aeiouAEIOU":
            words.append(input("Enter an " + i + ": "))
        else:
            words.append(input("Enter a " + i + ": "))
    
    return words

def remove_blanks(source):
    """Removes the blanks from the source and returns the source as a list"""

    words = []
    current_word = ""
    currently_adding = True

    for i in source:
        if i == ">":
            currently_adding = True
            continue
        if i == "<":
            currently_adding = False
            words.append(current_word)
            current_word = ""
        if currently_adding:
            current_word += i

    if current_word != "":
        words.append(current_word)

    return words

def reassemble_source(source, words):
    """Once the blanks have been removed from the source, reassembles it with the user-inputted words"""

    final = ""

    for i in range(len(source)):
        final += source[i]
        try:
            final += words[i]
        except:
            pass
    
    return final

blanks = locate_blanks(source)
source = remove_blanks(source)
words = get_words(blanks)
final = reassemble_source(source, words)

print(final)