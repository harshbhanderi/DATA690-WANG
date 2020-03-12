# 602 Assignment 2
# By Harsh Bhanderi

# Import library to generate random numbers
import random

# loop for number of rows
for i in range(0, 12):

    # loop for number of columns
    for j in range(0, 12):

        # defining first and last row to asterisks(*)
        if i == 0 or i == 11:
            print('*    ', end='')

        # for all other rows prints first and last element as asterisk(*)
        elif j == 0 or j == 11:
            print('*    ', end='')

        # generate random integers from 0 to 9 for all other positions like for middle 10*10 matrix
        else:
            print(random.randint(0,9), '   ', end='')
    # End of rows
    print('\n')
