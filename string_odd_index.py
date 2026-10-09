def odd_index(word):
    result = ""
    for character in range(len(word)):
        if character % 2 == 1:
            result += word[character]
    return result
    
print(odd_index("dave"))
