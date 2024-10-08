addIns = ["whipped cream", "cinnamon", "chocolate sauce", "amaretto", "irish whiskey"]
prices = [0.89, 0.25, 0.59, 1.50, 1.75]
baseCoffeePrice = 2.00
totalPrice = baseCoffeePrice

def availableMenu():
    print("\nWelcome to Jumpin' Jive Coffee Shop")
    print(f"\nOur base price for coffee is ${baseCoffeePrice}")
    print("Our available add-ins are:")
    for i in range(len(addIns)):
        print(f"\n{addIns[i]} - ${prices[i]:.2f}")

availableMenu()

while True:
    userAddIn = input("\nEnter an add-in (or type 'done' to complete the order): ")

    if userAddIn == 'done':
        break

    if userAddIn in addIns:
        index = addIns.index(userAddIn)
        addInPrice = prices[index]
        totalPrice += addInPrice
        print(f"{userAddIn} added for ${addInPrice:.2f}")
    else:
        print("Sorry, we do not carry that.")

print(f"\nThe total price for your coffee order is: ${totalPrice:.2f}")
print("\nThank you for choosing Jumpin' Jive Coffee Shop.\nYour order will be ready soon!")


    

        