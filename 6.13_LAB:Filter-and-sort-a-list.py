# 6.13 LAB: Filter and sort a list

# Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).
#
# Ex: If the input is:
#
# 10 -7 4 39 -6 12 2
# the output is:
#
# 2 4 10 12 39
# For coding simplicity, follow every output value by a space. Do not end with newline.

new_list = ([])
list = input("Enter your numbers: ").split()

# TODO - ask how this could have been written using a list comprehension

for i in list:
    if int(i) >= 0:
        new_list.append(int(i))
        new_list.sort()
for x in new_list:
    print(x, end=' ')
