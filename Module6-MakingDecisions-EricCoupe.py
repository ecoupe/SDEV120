# Imported 'sys' for the option of closing the program when exiting the final loop
import sys

customerData = []   # This creates an open list to store the customer data
while True:     # First while loop. Kept it open with 'True' so user can repeat data entry
    baseFee = 5
    taxRate = 0.14
    areaCode = input("Please enter a 3 digit area code: ")
    while not (len(areaCode) == 3 and areaCode.isdigit()):  # This limits the input length to 3 digits
      areaCode = input("Please enter a 3 digit area code: ")
    phoneNumber = input("Please enter a 7 digit phone number: ")
    while not (len(phoneNumber) == 7 and phoneNumber.isdigit()):    # This limits the input length to 7 digits
      phoneNumber = input("Please enter a 7 digit phone number: ")
    textMessages = int(input("Please enter number of sent text messages (100 or more): "))

    if textMessages > 100 <= 300:   # From here to line 23 is processing of the assignment requirements
        textFee1 = (textMessages-100) * .03
    bills = baseFee + textFee1
    if textMessages > 300:
        textFee2 = (textMessages-300) * .02
    bills = baseFee + textFee1 + textFee2  

    totalBills = bills * taxRate

    if textMessages > 100:  # This prints customer info after more than 100 text messages are sent
        print(f"\nYou have sent {textMessages} messages this month.")
    print(f"Your phone number is {areaCode} {phoneNumber}")

    if totalBills > 10: #This prints only when the customer bill is over $10
        print(f"\nYour text message fee is ${textFee1: .2f} plus ${textFee2: .2f}")
    print(f"Your monthly bill before taxes is ${bills: .2f}.")
    print(f"Your total bill is ${totalBills: .2f}.")

    customerData.append({       # This adds user supplied data to the 'customerData' list after processing
            'area_code': areaCode,
            'phone_number': phoneNumber,
            'text_messages': textMessages,
            'bill_before_tax': bills,
            'total_bill': totalBills
        })

    additionalCustomers = input("Do you want to enter another customer? (yes/no): ")    # Asks the user if there is more data to input
    if additionalCustomers.lower() != 'yes':
        break

# Another open while loop. Prompts the user for an area code stored in 'customerData' list to view the associated bill
while True: 
    areaCodeFilter = input("\nEnter a 3 digit area code to view bills from that specific area: ")
    for customer in customerData:
        if customer['area_code'] == areaCodeFilter: # This calls a category from the 'customerData' list
            print(f"\nArea Code: {customer['area_code']} \nPhone Number: {customer['phone_number']} "
                  f"\nMessages: {customer['text_messages']} \nBill Before Tax: ${customer['bill_before_tax']: .2f} "
                  f"\nTotal Bill: ${customer['total_bill']: .2f}")
    
    moreAreaCodes = input("Would you like to view another area code? (yes/no) ")    # Asks the user if another area code/bill should be viewed
    if moreAreaCodes == 'yes':
        continue
    if moreAreaCodes.lower() != 'yes':
        sys.exit()  # Utilizes 'sys' import to close the program







