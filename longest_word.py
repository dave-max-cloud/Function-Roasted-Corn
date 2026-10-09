def longest_word(words):
    longest = " "
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest, len(longest)
    
the_list = ["welcome","out","weather","mobile","breakfast","journey"] 
result_word, result_length = longest_word(the_list) 

print(result_word)
