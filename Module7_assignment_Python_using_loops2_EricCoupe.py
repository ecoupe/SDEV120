# List of 15 numbers
numbersList = [7, 41, 50, 5, 35, 10, 34, 23, 8, 1, 43, 31, 30, 36, 39]

# Loop for going through the list of numbers
# Removed user input to better match assignment requirements
for number in numbersList:

# Here is the check for if the numbers are even or odd
    if (number %2 ==0):
        print(str(number) + " is even!")
    else:
        print(str(number) + " is odd!")