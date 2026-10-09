def minimum_numbers(numbers):
    smallest = numbers[0]
    for the_number in numbers:
        if the_number < smallest:
            smallest = the_number
    return smallest
print(minimum_numbers([8,4,9,2,5,7,3]))
