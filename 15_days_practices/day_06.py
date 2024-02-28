# learning day 06 - LISTS AND TUPLES

# 1) Given two lists of numbers, concatenate them into a single list
a = [3, 45, 34, 78, 1, 12]
b = [12, 456, 67, 3]
c = a + b
c.sort()
print(c)

# 2) Write a program that finds the largest and smallest elements in a list. 
elements = [1, 3, 3, 12, 12, 34, 45, 67, 78, 456]
max_elem = max(elements)
min_elem = min(elements)
print(f"this is the largest number: {max_elem} and this is the smallest number: {min_elem}")

# 3) Implement a function that takes a list of numbers and returns a new list with the squared values. 
numbers = [12, 456, 67, 3]


def squared_values(numbers):
    return [i ** 2 for i in numbers]


result = squared_values(numbers)
print(result)

# 4) Create a program that finds the common elements between two lists and stores them in a new list. 
a = [3, 45, 34, 78, 67, 1, 12]
b = [12, 456, 34, 67, 3]


def find_common(a, b):
    result = [i for i in a if i in b]
    return result


result = find_common(a, b)
print(f"these are the common elements: {result}")

# 5) Given a list of numbers, find the sum and average using built-in functions.
a = [3, 45, 34, 78, 67, 1, 12]
b = [12, 456, 34, 67, 3]
c = a + b
sum_v = sum(c)
avg_v = sum(c) / len(c)
print(f"this is the sum of the number: {sum_v} and this is the average: {avg_v}")

# 6) Create a list of fruits and add a new fruit to the list.

fruits = ["apple", "banana", "kiwi"]
fruits.append("raspberry")
print(fruits)

# 7) Access elements in a tuple using indexing.
fruits = ['apple', 'banana', 'kiwi', 'raspberry']
print(fruits[2])

# 8) Implement a function that takes two lists and returns their union (all unique elements from both lists).
a = [3, 45, 34, 78, 67, 1, 12]
b = [12, 456, 34, 67, 3]


def union_list(a, b):
    new_list = a + b
    new_list.sort()
    return new_list


result = union_list(a, b)
print(result)
