def maximum_numbers(numbers):
    largest = numbers[0]
    for the_number in numbers:
        if the_number > largest:
            largest = the_number
    return largest
    
print(maximum_numbers([8,4,9,2,5,7,3]))
