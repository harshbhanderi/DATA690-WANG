# 690 : Assignment 1
# Harsh Bhanderi

# importing library
import statistics

# function to get input from user
def inputNumber():
    while True:
        try:
            # takes only integer input
            user_input = int(input())
        # raise an error if value is not an integer and let user try again
        except ValueError:
            print('Not an Integer!! Try again..')
            continue
        else:
            return user_input
        break

# empty list to save all the input numbers
numbers = []

# for loop to get only 10 numbers
for i in range(0, 10):
    print("Enter Number ", (i + 1), " : ")

    numbers.append(inputNumber())

# Listed the 10 input numbers
print("Input Numbers are : ", numbers)

# maximum number
max_number = max(numbers)
print("Max : ", max_number)

# minimum number
min_number = min(numbers)
print("Max : ", min_number)

# range of numbers
range_list = max_number - min_number
print("Range : ", range_list)

# mean of numbers
mean = statistics.mean(numbers)
print("Mean : ", mean)

# variance of numbers
var = statistics.pvariance(numbers)
print("Variance : ", var)

# standard deviation of numbers
var = statistics.pstdev(numbers)
print("Variance : ", var)

