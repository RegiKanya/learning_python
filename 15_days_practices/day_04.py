# learning python day 4 - FUNCTIONS

# 1) Given a list of numbers, create a function to find the sum of all positive numbers. 
list_of_num = [34, 23, 12, -3, 56, 0, 99, 1, 3, -14]
# a = sum(num for num in list_of_num if num > 0)
# print(a)


def sum_pos_num(list_of_num):
    num = 0
    for i in list_of_num:
        if i > 0:
            num += i
    return num


result = sum_pos_num(list_of_num)  # hiba: csak úgy meghívtam a function-t és így nem mutatta a tényleges eredményt
print(result)

# 2) Implement a function that returns the factorial of a given number using recursion. 

# 3) Create a function to find the square of each element in a given list. 
list = [5, 45, 6, 12, 9]


def find_square(list):
    return [i ** 2 for i in list]


result = find_square(list)
print(f"these are the square values of the elements: {result}")

# 4) Create a function that takes a list of strings and returns the list sorted alphabetically. 
list_of_strings = ["d", "h", "b", "a", "c", "f", "e", "g"]


def sort_in_abc(list_of_strings):
    abc = sorted(list_of_strings)
    return abc


result = sort_in_abc(list_of_strings)
print(f"this is the alphabetical order: {result}")

# 5) Write a function that takes two lists and returns their intersection (common elements). 
list_1 = {"anna", "jános", "tamás", "józsi", "viki"}
list_2 = {"nóra" , "tamás", "viki", "károly"}


def common_element(list_1, list_2):
    intersec = list_1.intersection(list_2)
    return intersec


result = common_element(list_1, list_2)
print(f"common elements: {result}")

# 6) Create a function that takes a number as input and prints its multiplication table.
num = int(input("which number's multiplication table do you want to see?"))


def print_multi_table(num):
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i)


print_multi_table(num)

