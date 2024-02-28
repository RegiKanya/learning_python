# day 2 projects - VARIABLES AND DATA TYPES

# 1) Given a list of numbers, find the sum and average. 
numbers = [56, 34, 123, 66, 76, 1, 34]
sum_of_num = sum(numbers)
avg_of_num = sum_of_num / len(numbers)
print(f"this is the sum value: {sum_of_num}")
print(f"this is the average: {avg_of_num}")

# 2) Create a program that takes a temperature in Celsius and converts it to Kelvin. 
temperature = int(input("What's the temperature that you want to convert?"))
fahrenheit = (1.8 * temperature) + 32
print(f"this is the converted value of Celsius to Fahrenheit: {fahrenheit}")


# 3) Create a function to reverse a given string. 
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "kánya regina"
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using loops) is : ", end="")
print(reverse(s))
# ------------------------


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = "kánya regina"
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using recursion) is : ", end="")
print(reverse(s))

# 4) Given a list of names, concatenate them into a single string separated by spaces.


def convert(lst):
    return ' '.join(lst)


lst = ['Regi', 'is', 'learning', 'Python']
print(convert(lst))

# 5) Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).

import string


def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
 
    return True


string = 'The quick brown fox jumps over a lazy dog'

if( ispangram(string) == True ):
    print("Yes")
else:
    print("No")

# 6) Calculate the area and circumference of a circle given its radius. 
pi = 3.141
radius = int(input("What is the radius of the circle?"))
area = (pi * (radius ** 2))
circumference = (2 * radius * pi)
print(f"this is the area of a circle: {area}")
print(f"this is the circumference of a circle: {circumference}")


# 7) Create a function to count the number of vowels in a given string. 
String = input('Enter the string : ')
count = 0

String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are : ' + str(count))

# 8) Write a program to check if a number is prime.
is_prime = int(input("which number do you wanna check?"))
print(is_prime)


def get_factors(number):
    factors = []
    iteration_index = 1
    while iteration_index <= number:
        if number % iteration_index == 0:
            factors.append(iteration_index)
        iteration_index += 1
    print(f'the factors of {number} are: {factors}')
    return factors


def check_prime(number, factors):
    if len(factors) == 2:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')


def analyze_number(number):
    factors = get_factors(number)
    check_prime(number, factors)


analyze_number(is_prime)