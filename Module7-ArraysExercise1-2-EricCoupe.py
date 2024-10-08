userInput = []  #open array to store future input

print("Please enter 20 numbers: ")

for i in range(1, 21):  #using a range as sentinel number
    while True:
        try:
            #prompt will continue until sentinel number reached
            promptUser = int(input(f"Enter number {i}: ")) 
            userInput.append(promptUser)
            break
        except ValueError:  #error catcher to keep input as integers
            print("Please enter a valid number.")

print("\nHere are the numbers in reverse order: ")
for promptUser in reversed(userInput):
    print(promptUser)

