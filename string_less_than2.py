def last_word(word):
    if len(word) > 2:
        return word[:2] + word[-2:]
    elif len(word) == 2:
        return word + word
    else:
        return " "
print(last_word("Se"))
