# course: DSC510
# assignment: 3.1
# date: 03/29/2020
# name: Arindam Samanta
# description: Implementing "if" statements in a program

# Display a welcome message for your user.
print ( 'Welcome to Fiber Optic Store Online \n' )

# Retrieve the company name from the user
print ( 'What is the name of your company?\n' )
CompName = input ()

# print(CompName)

# Retrieve the number of feet of fiber optic cable to be installed from the user.
print ( 'What is the length of the cable?\n' )
CabLen = input()


# Cost of Cable needed
if (CabLen > 100 and CabLen <= 250):
    CabCost = round ( float ( CabLen ) * 0.80, 2 )
    print('Total cost for' + CabLen + '-'  + CabCost + '\n')
elif (CabLen > 250 and CabLen <= 500):
    CabCost = round ( float ( CabLen ) * 0.70, 2 )
    print('Total cost for' + CabLen + '-'  + CabCost + '\n')
elif CabLen > 500:
    CabCost = round ( float ( CabLen ) * 0.50, 2 )
    print('Total cost for' + CabLen + '-'  + CabCost + '\n')
else:
    CabCost = round ( float ( CabLen ) * 0.87, 2 )
    print('Total cost for' + CabLen + '-'  + CabCost + '\n')

# Total Cost of Installation

TotCost = CabCost + (CabCost * TaxRate) + LabCost
print ( 'INVOICE for ' + CompName + '\n')
print ( 'Fiber Optic Store Online \n' )
print ( 'Length of Fiber Optic Cable Ordered: ' + CabLen + ' ft' )
print ( 'Cost of Cable: ' + '$' + str ( CabCost ) )



