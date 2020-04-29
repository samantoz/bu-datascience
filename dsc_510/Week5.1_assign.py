# course: DSC510
# assignment: 5.1
# date: 04/11/2020
# name: Arindam Samanta
# description: This program will perform various calculations using loops and functions

# This Function will take in the type of operation user wants to perform
def performCalculation(operation):
    num1 = 0
    num2 = 0
    out1 = 0

    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    if operation == 1:
        out1 = num1 + num2
    elif operation == 2:
        out1 = num1 - num2
    elif operation == 3:
        out1 = num1 * num2
    elif operation == 4:
        if num2 == 0:
            print("Invalid Value!")
        else:
            out1 = num1 / num2
    return (out1)

# This function will perform average of the input numbers from user
def calculateAverage():
    inputNum = []  # initializing and empty list to hold the numbers.
    sum1 = 0
    avg = 0
    ctr = int(input("Please enter the count of numbers you wish to input: "))
    for i in range(0, ctr):
        numbers = int(input("Enter your choice number " + str(i + 1) + ": "))
        inputNum.append(numbers)
        sum1 = sum1 + numbers
    avg = sum1 / ctr
    return (avg)


def main():

    while True:
        print("Please enter the calculation you wish to perform('addition: 1','subtraction: 2','multiplication: 3',"
              "'division: 4','average: 5') : \n")
        try:
            oper = int(input())
            break
        except ValueError:
            print("Sorry, I didn't understand that.Try again")
            continue
    if oper == 1:  # Verify the input value to decide the operation
        print("Sum of two the numbers is: " + format(performCalculation(oper), '.2f'))
    #     print(oper)
    elif oper == 2:
        print("Difference of the two numbers is: " + format(performCalculation(oper),'.2f'))
    #     print(oper)
    elif oper == 3:
        print("Product of the two numbers is: " + format(performCalculation(oper),'.2f'))
    #     print(oper)
    elif oper == 4:
        print("Quotient of the two numbers is: " + format(performCalculation(oper),'.2f'))
    #     print(oper)
    elif oper == 5:
        print(format(calculateAverage(), '.2f'))
    else:
        print("Invalid value. Exiting program.")


if __name__ == "__main__":
    main()
