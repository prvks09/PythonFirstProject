import math
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# i = 3
# print("Hello World  😊")
# print("* * * " * 10)
# print("Hello World")

# i = 2
# print(i)
# if i < 5:
#     print("i is less than 5")
# else:
#     print("i is 5 or more")
# k = 3
# print(len("Hello World"))

# course = "Python Programming"
# # course[1] = "J"
# print(course)
# course1 = "Python \\Programming"
# print(course1)
# course2 = "Python \nProgramming"
# print(course2)
# course3 = "Python \\nProgramming"
# print(course3)
# first = "Vikas"
# last = "Puri"
# full = first + " " + last
# print(full)
# full_name = f"{first} {last} is learning Python"
# print(full_name)
# print(full_name.capitalize())
# print(full_name.upper())
# print(full_name.isupper())
# print(full_name)

# x = 3
# x += 2
# print(x)

# y = 3.3
# print(math.ceil(y))

# temperature = 5
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature < 10:
#     print("It's a cold day")
# print("Enjoy your day")
# high_score = True
# good_credits = True
# student = True
# if high_score and good_credits and student:
#     print("You get a scholarship")
# message = "Eigible" if high_score and good_credits and student else "Not eligible"
# print(message)


def my_print():
    print("Hello from my_print function")


my_print()


def bubble_sort(scores):
    n = len(scores)
    for i in range(n):
        for j in range(0, n-i-1):
            logging.debug(f"Input i: {i}, j : {j}, j+1: {j+1}, List {scores}")
            if scores[j] > scores[j+1]:
                logging.debug(
                    f"Swap j : {j}, value = {scores[j]}, j+1: {j+1}, value = {scores[j+1]}")
                # scores[i], scores[j] = scores[j], scores[i]
                temp = scores[j]
                scores[j] = scores[j+1]
                scores[j+1] = temp

            logging.debug(f"Output i: {i}, j : {j}, j+1: {j+1}, List {scores}")
    return scores


scores = [87, 90, 75, 100, 100, 70]

sorted_scores = bubble_sort(scores)
highest_score = max(sorted_scores)
lowest_score = min(sorted_scores)
print(f"Sorted Scores: {sorted_scores}")
print(f"Highest Score: {highest_score}")
print("Hi How are you ")
print(f"Lowest Score: {lowest_score}")
print("This is a change to test git")
