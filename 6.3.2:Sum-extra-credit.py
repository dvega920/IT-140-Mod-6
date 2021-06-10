# 6.3.2: Sum extra credit.

# Assign sum_extra with the total extra credit received given list test_grades. Full credit is 100, so anything over 100 is extra credit.
#
# Sample output for the given program with input: '101 83 107 90'
# Sum extra: 8
# (because 1 + 0 + 7 + 0 is 8)


user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores
sum_extra = 0 # Initialize 0 before your loop

print(test_grades)

for grade in test_grades:
    if grade > 100:
        extra_credit = grade - 100
        sum_extra += extra_credit

print('Sum extra:', sum_extra)
