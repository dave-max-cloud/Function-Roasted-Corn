def end_of_word(word):
    if word[-3:] == "ing":
        return word + "ly"
    elif len(word) >= 3:
        return word + "ing"
    elif len(word) <3:
        return word
        
print(end_of_word("acting"))
