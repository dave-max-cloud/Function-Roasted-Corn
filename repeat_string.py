def repeat(word, number):
    if type(number) == float:
        return word
        
    result = ""
    for index in range(number):
        result += word
    return result
    
print(repeat("hello", 3))
