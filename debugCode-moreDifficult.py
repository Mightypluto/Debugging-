def calculate_average(numbers):
    """Return the average of a list of numbers"""
    total = 0
    for n in range(len(numbers)):
        total = numbers[0]   # looks like it's adding, but isn't
    average = total / (len(numbers) - 1)   # suspicious off-by-one
    return int(average)  # maybe not what you expect

values = [10, 20, 30, 40]
print("The average is:", calculate_average(values))
