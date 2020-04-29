# course: DSC510
# assignment: 6.1
# date: 04/18/2020
# name: Arindam Samanta
# description: This program will work with lists.

temperatures = []  # Initializing an empty list

# Stop when temp == -999
# Sentinel value is -999 to stop user input
temp = 0
while(temp > -999): # This loop will populate the list
    temp = float(input("Please enter the temperature(-999 to end the list): "))  # Getting the user input
    if temp > -999:  # -99 is the sentinel value when the list stops populating
        temperatures.append(temp)

L = temperatures  # Assigning the list to a variable
L.sort() # Sorting the list so that the minimum value is first
print("The largest temperature in your list is :" + str(L[-1]))
print("The smallest temperature in your list is :" + str(L[0]))
print("The list has " + str(len(L)) + " temperatures.")






