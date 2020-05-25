#!/usr/bin/env python
# coding: utf-8

# In[28]:


# course: DSC510
# assignment: 4.1
# date: 04/04/2020
# name: Arindam Samanta
# description: Implementing functions in a program

# Display a welcome message for your user.
print ( 'Welcome to Fiber Optic Store Online \n' )

# Retrieve the company name from the user
print ( 'What is the name of your company?\n' )
CompName = input ()

# print(CompName)

# Defining a function here

def CabCostFunc( CabLength, unitCost):
    iCost = CabLength * unitCost
    tax = 0.075 * iCost

    print (format (iCost, '.2f'))

    print ( 'Length of Fiber Optic Cable Ordered: ' + format(CabLength, '.2f') + ' ft' )
    print ( 'Cable Cost                 @' + format(unitCost, '.2f') + '   : ' + '$' + format(iCost, '.2f') )
    print ( 'Tax (7.5%)                         : ' + '$' + format(tax,'.2f'))
    print ( 'Total Cost of Cable                : ' + '$' + format((iCost + tax),'.2f'))
    

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

print ( 'INVOICE for ' + CompName )
print ( 'Fiber Optic Store Online \n' )

CabCostFunc(CabLen,CabCost)
