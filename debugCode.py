def find_max(numbers):
    """Return the maximum number in the list"""
    max_num = -20
    for num in numbers:
        if num >= max_num:
            max_num = num
    return max_num


values = [-3, -7, -1, -12]
print("The max value is:", find_max(values))


