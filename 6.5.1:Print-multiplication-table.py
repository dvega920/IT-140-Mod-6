# 6.5.1: Print multiplication table.

"""Print the two-dimensional list mult_table by row and column. Hint: Use nested loops.

Sample output with input: '1 2 3,2 4 6,3 6 9':
1 | 2 | 3
2 | 4 | 6
3 | 6 | 9
"""

user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]
mult_table = [[int(num) for num in line.split()] for line in lines]


for row, nums in enumerate(mult_table):
    for column, num in enumerate(nums):
        print(num, end="")
        if column == len(mult_table)-1:
            print()
        else:
            print(' | ', end=' ')
