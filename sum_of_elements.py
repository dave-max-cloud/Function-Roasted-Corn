def sum_of_elements(numbers):
    total = 0
    for the_numbers in numbers:
        total += (the_numbers * the_numbers)
    return total
    
print(sum_of_elements([2,3,4,5,7]))
