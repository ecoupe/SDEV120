# List of 15 numbers
numbersList = [7, 41, 50, 5, 35, 10, 34, 23, 8, 1, 43, 31, 30, 36, 39]

# Loop for going through the list of numbers
# Adds user input to slow the loop
for number in numbersList:
    input("Press Enter to check the next number in the list")

# Here is the check for if the numbers are even or odd
    if (number %2 ==0):
        print(str(number) + " is even!")
    else:
        print(str(number) + " is odd!")