"""Its mad libs"""

source = "It was a cold, <adjective> November day. I woke up to the <adjective> smell of <type of bird> roasting in the <room in a house> downstairs. I <verb (past tense)> down the stairs to see if I could help <verb> the dinner. My mom said \"See if <name> needs a fresh <noun>.\" So I carried a tray of glasses full of <liquid> into the <verb ending in -ing> room. When I got there, I couldn\'t believe my <part of the body (plural)>! There were <plural noun> <verb ending in -ing> on the <noun>!"

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