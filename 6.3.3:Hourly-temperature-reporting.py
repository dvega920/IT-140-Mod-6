# 6.3.3: Hourly temperature reporting.
# Write a loop to print all elements in hourly_temperature. Separate elements with a -> surrounded by spaces.
#
# Sample output for the given program with input: '90 92 94 95'
# 90 -> 92 -> 94 -> 95
# Note: 95 is followed by a space, then a newline.


user_input = input()
hourly_temperature = user_input.split()
string = []
for temp in hourly_temperature:  # iterates through hourly_temperature
    string.append(temp)  # Appends temp to empty string list
print(' -> '.join(string), end=' ')  # joins the string list with ' -> ' and ends each string with a space
print()  # prints a new line
