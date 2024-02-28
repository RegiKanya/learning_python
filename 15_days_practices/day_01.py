# day 1 projects - INTRODUCTION AND SETUP

# 1) Write a Python program to calculate the area of a rectangle given its length and width.
rectangle_length = 11
rectangle_width = 28
area_of_rectangle = rectangle_length * rectangle_width
print(f"This is the area of the rectangle: {area_of_rectangle}")

# 2) Create a program that takes a user's name and age as input and prints a greeting message.
name = input("What's your name?")
age = input("How old are you?")
print(f"Hello {name}, {age}")

# 3) Write a program to check if a number is even or odd.
value = int(input("What's number do you wanna check?"))
print(f"Checking: {value}")


def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")


check_even_odd(value)

# 4) Given a list of numbers, find the maximum and minimum values.
list_numbers = [3, 45, 678, 2, 356, 99, 10, 12, 1234, 546]
max_number = max(list_numbers)
min_number = min(list_numbers)
print(max_number)
print(min_number)


# 5) Create a Python function to check if a given string is a palindrome.
def check_palindrome(value):
    if value == value[::-1]:
        return True
    return False


run = True
while run:
    word = input("Choose a word to check:")
    if word == "exit":
        run = False
        break

    word = word.lower()

    newstr = ""
    for x in word:
        if x.isalnum():
            newstr += x

    print("Palindrome test:", check_palindrome(newstr))

check_palindrome(word)


# 6) Calculate the compound interest for a given principal amount, interest rate, and time period.
def compound_interest(principal, rate, time):
    amount = principal * (pow((1 + rate / 100), time))
    CI = amount - principal
    print("Compound interest is", CI)


compound_interest(10000, 12.5, 5)

# 7) Write a program that converts a given number of days into years, weeks, and days.
given_day = 345670
years = given_day / 365
weeks = given_day / 7
print(f"the given days is {years} years")
print(f"the given days is {weeks} weeks")

# 8) Given a list of integers, find the sum of all positive numbers.
integers = [5, 4, 99, 567, 3, 45, 5]
sum_pos = sum(integers)
print(sum_pos)

# 9) Create a program that takes a sentence as input and counts the number of words in it.
text = input("what do you want to count?")
sentence_word = len(text.split())
print(sentence_word)

# # 10) Implement a program that swaps the values of two variables.
first = 3
second = 7

temp = first
first = second
second = temp

print(first)
print(second)

# other way
first = 3
second = 7

first, second = second, first

print(first)
print(second)
