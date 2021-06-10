# 6.12 LAB: Varied amount of input data
# Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.
#
# Ex: If the input is:
#
# 15 20 0 5
# the output is:
#
# 10 20
#
user_input = input()

# used list comprehensions to convert string numbers into integers. use sum() to sum the values of i and then divide by
# length of user_input.split() (floor result) and assign to variable avg.
avg = sum([int(i) for i in user_input.split()]) // len(user_input.split())

# used list comprehensions to convert string numbers into integers. use max() to find the maximum number in the list
max = max([int(i) for i in user_input.split()])

print(avg, max)
