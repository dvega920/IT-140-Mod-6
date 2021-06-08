# 6.3.1: Get user guesses.

"""Write a loop to populate the list user_guesses with a number of guesses. Each guess is an integer. Read integers using int(input()).

Sample output with input: '3 9 5 2'
user_guesses: [9, 5, 2]"""

num_guesses = int(input())
user_guesses = []

for i in range(num_guesses):
    num_guesses = int(input())
    user_guesses.append(num_guesses)
    print('user_guesses:', user_guesses)
