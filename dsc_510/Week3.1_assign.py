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
CabLen_str = input()
CabLen = float(CabLen_str)
CabCost = 0.00 # Initializing the cost

# Cost of Cable needed
if (CabLen > 100 and CabLen <= 250):
    CabCost = 0.80
elif (CabLen > 250 and CabLen <= 500):
    CabCost = 0.70
elif CabLen > 500:
    CabCost = 0.50
else:
    CabCost = 0.87

Cost = round(CabLen * CabCost,2)

# Total Cost of Installation
# print('Cable cost for length ' + CabLen_str + ' fit is ' + str(Cost))
tax = round((0.075 * Cost),2)
TotCost = round((Cost + tax),2)
# TotCost = CabCost + (CabCost * TaxRate) + LabCost
print ( 'INVOICE for ' + CompName + '\n')
print ( 'Fiber Optic Store Online \n' )
print ( 'Length of Fiber Optic Cable Ordered: ' + CabLen_str + ' ft' )
print ( 'Cable Cost                 @' + str(CabCost) + '   : ' + '$' + str(Cost))
print ( 'Tax (7.5%)                         : ' + '$' + str(tax))
print ( 'Total Cost of Cable                : ' + '$' + str ( TotCost ) )


