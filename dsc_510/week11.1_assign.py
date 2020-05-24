# course: DSC510
# assignment: 11.1
# date: 05/24/2020
# name: Arindam Samanta
'''

The program tries to emulate a CashRegister.
It also keep track of the number of items in your cart.
It prints the total number of items in the cart and the total $ amount of the cart.
The output should be formatted as currency.
'''

import locale


class CashRegister:

    def __init__(self):  # Initializing the variables
        self.totalPrice = 0.00
        self.itemCount = 0

    def addItem(self, price):  # adds item to register
        self.totalPrice += price
        self.itemCount += 1

    def getTotal(self):  # return total price
        return self.totalPrice

    def getCount(self):  # return count of items
        return self.itemCount

    def clear(self):  # reset register to zero
        self.totalPrice = 0.00
        self.itemCount = 0


'''
The below function takes in the user response and checks if the user response is alpha or numeric
'''


def is_numeric(n):
    try:
        float(n)  # type-casting the string to 'float',if string is not a valid float or integer it will
                  # raise value error
    except ValueError:
        return False  # the user input is alpha
    return True


def main():
    print("Welcome to the General Store!")
    cr = CashRegister()  # instantiating the class
    locale.setlocale(locale.LC_ALL, '')
    user_response = input(
        "Please enter the price to add an item to your cart, or ""exit"" to exit. ""empty"" will clear "
        "your cart \n"
        "Price : ")
    while is_numeric(user_response):
        price = float(user_response)
        # print(" You start count : ", cr.getCount())
        # print(" Your Total Price to start : ", cr.getTotal())
        cr.addItem(price)  # Adding the item with the price
        print(" You now have " + str(cr.getCount()) + " items in your cart.")
        print(" Your Total Price is currently : ", locale.currency(cr.getTotal()))

        user_response = input(
            "Please enter the next price to add an item to your cart, or ""exit"" to exit. ""empty"" will clear "
            "your cart \n"
            "Price :")
    else:
        # this part will be executed if the user response is not numeric.
        if user_response == 'exit':
            print("Please proceed to check out")
        elif user_response == '':
            cr.clear()
            print("Good bye!")
            print("Your shopping cart is cleared. Please start again.")
        else:
            cr.clear()
            print("Please enter a valid input.")

    print(" You have " + str(cr.getCount()) + " items in total.")
    print(" Your Total Price is: ", locale.currency(cr.getTotal()))
    cr.clear()


if __name__ == '__main__':
    main()
