userInput = []  #open array for future input

while True:     #open loop to repeat input
    promptUser = input(("Please enter 20 numbers (enter 'done' to finish): "))

    if promptUser == 'done':    #stopping the loop
        break

    try:
        i = int(promptUser) #temp variable to add input to array
        userInput.append(i)
    except ValueError:      #error catcher to keep input as integers
        print("Please enter a number.")

print("\nHere are the numbers in reverse order: ")

for num in reversed(userInput):
    print(num)

