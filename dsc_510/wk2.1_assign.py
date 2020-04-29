# course: DSC510
# assignment: 2.1
# date: 03/20/2020
# name: Arindam Samanta
# description: Program to calculate cost of cable.

# Display a welcome message for your user.
print ( 'Welcome to Fiber Optic Store Online \n' )

# Retrieve the company name from the user
print ( 'What is the name of your company?\n' )
CompName = input ()

# print(CompName)

# Retrieve the number of feet of fiber optic cable to be installed from the user.
print ( 'What is the length of the cable?\n' )
CabLen = input ()
# Cost of Cable needed
CabCost = round ( float ( CabLen ) * 0.87, 2 )

# Tax and Labor Cost
TaxRate = 0.7
LabCost = 70.00
# Total Cost of Installation

TotCost = CabCost + (CabCost * TaxRate) + LabCost
print ( 'INVOICE for ' + CompName + '\n')
print ( 'Fiber Optic Store Online \n' )
print ( 'Length of Fiber Optic Cable Ordered: ' + CabLen + ' ft' )
print ( 'Cost of Cable: ' + '$' + str ( CabCost ) )
print('Total Cost of Installation: ' + str(TotCost))
