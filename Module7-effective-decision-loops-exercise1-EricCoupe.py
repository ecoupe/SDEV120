# This program will ask for a series of integers. The integers will be stored in
# an array. When the user inputs the sentinel number, the program will
# add the contents of the array together and output the sum.

numbersArray=[]

while True:     # open while loop to repeat the inputs until sentinel number
    numbersRequest = int(input("Please enter a series of integers. Press '0' to exit: "))
    
    if numbersRequest == 0:     # when the sentinel number is input, add the array contents
        addition = sum(numbersArray)
        print(f"\nThe total sum of your integers is: {addition}")
        break
    else:
        numbersArray.append(numbersRequest)     # repeats the loop while storing integers in the array
    
    
    


    