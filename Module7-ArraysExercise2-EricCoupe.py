addIns = ["whipped cream", "cinnamon", "chocolate sauce", "amaretto", "irish whiskey"] #two seperate arrays
prices = [0.89, 0.25, 0.59, 1.50, 1.75]
baseCoffeePrice = 2.00
totalPrice = baseCoffeePrice

def availableMenu():    #function to display a menu for the user
    print("\nWelcome to Jumpin' Jive Coffee Shop")
    print(f"\nOur base price for coffee is ${baseCoffeePrice}")
    print("Our available add-ins are:")
    for i in range(len(addIns)):
        print(f"\n{addIns[i]} - ${prices[i]:.2f}")  #format output as float with 2 decimal points

availableMenu() #execute function

while True: #main processing loop. open for continuous input
    userAddIn = input("\nEnter an add-in (or type 'done' to complete the order): ")

    if userAddIn == 'done': #sentinel value
        break

    if userAddIn in addIns: #this for loop helps find the location of the user input within the arrays
        index = addIns.index(userAddIn)
        addInPrice = prices[index]
        totalPrice += addInPrice
        print(f"{userAddIn} added for ${addInPrice:.2f}")
    else:
        print("Sorry, we do not carry that.")

print(f"\nThe total price for your coffee order is: ${totalPrice:.2f}")
print("\nThank you for choosing Jumpin' Jive Coffee Shop.\nYour order will be ready soon!")


    

        