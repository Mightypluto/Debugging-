def find_max(numbers):
    """Return the maximum number in the list"""
    max_num = -20 #if zero does n0t work for neg numbers in list
    for num in numbers:
        if num >= max_num:
            max_num = num
    return max_num #max_Num


values = [-3, -7, -1, -12]
print("The max value is:", find_max(values))

#Isaac



