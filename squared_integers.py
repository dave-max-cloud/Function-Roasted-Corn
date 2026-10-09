def square(numbers):
    result = []
    for the_numbers in numbers:
        result.append(the_numbers * the_numbers)
    return result
    
print(square([2,3,4,5,7]))
