def calculate_average(numbers):
    """Return the average of a list of numbers"""
    total = 0
    for n in range(len(numbers)):
        total = total + numbers[n]   # looks like it's adding, but isn't
    average = total / (len(numbers))   # -1 does nothing
    return int(average)  
values = [10, 20, 30, 40]
print("The average is:", calculate_average(values))

#Lets add more numbers and make the user tell witch ones they want

