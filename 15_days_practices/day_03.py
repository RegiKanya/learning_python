# practising python codes day 3 - CONTROL FLOW AND LOOPS

# 1) Create a program that takes a year as input and checks if it is a leap year or not. 
number = int(input("what's year do you want to check?"))
# print(number)

def check_leap_years(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(f"{number} is leap year")
    else:
        print(f"{number} is not a leap year")

check_leap_years(number)

# 2) Given a list of integers, find all the even numbers and store them in a new list. 
integers = [33, 23, 45, 78, 2, 11, 77, 89, 56, 10, 13, 189]

for num in integers:
    if num % 2 == 0:
        print(num, end=" ")

# 3) Create a program that generates the Fibonacci sequence up to a given number of terms.
number = int(input("how many fibonacci sequence values would you like to see?"))

n = number
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

# 4) Given a list of names, print all names starting with the letter 'A'. 
names = ["Anna", "Tamas", "Judit", "Viktor", "Regina", "Alma", "Aranka"]

for name in names:
    if name.startswith('A'):
        print(name)

# 5) Implement a program that prints the multiplication table of a given number. 


# 6)  Write a program that calculates the factorial of a given number. 
num = int(input("What's your number?"))

def get_factors(number):
    factors = [ ]
    iteration_index = 1 
    while iteration_index <= number:
        if number % iteration_index == 0:
            factors.append(iteration_index)
        iteration_index += 1
    print(f'The factors of {num} are: {factors}')
    return factors

get_factors(num)

# 7) Create a loop that prints all prime numbers between 1 and 50. 
from_num = int(input('Start counting from: '))
until_num = int(input('End counting at: '))
print("The range of the prime numbers: ")
for number in range (from_num, until_num + 1):
    # all prime numbers are greater than 1
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else: 
            print(number)

# 8) Calculate the sum of digits of a given number.
given_number = int(input("What's your number?"))
def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
print(getSum(given_number))
