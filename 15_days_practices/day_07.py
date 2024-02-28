# learning day 07 - Dictionaries and Sets

# 1) Create a dictionary to store information about a person (name, age, address).
person_1 = {
    "name": "Melissa",
    "age": "24",
    "address": "Brooklyn street 26"
}

print(person_1)

# 2) Add a new key-value pair to an existing dictionary.

person_2 = {'name': 'John', 'age': '28', 'address': 'New York 1234'}
person_1.update(person_2)

# print(person_1)

new_key_name = 'name'
new_value_name = 'John'
new_key_age = 'age'
new_value_age = '28'
new_key_address = 'address'
new_value_address = 'New York 1234'

updated_dict = {**person_1, new_key_name: new_value_name, new_key_age: new_value_age, new_key_address:new_value_address}
print(updated_dict)

# 3)Create a set of unique numbers from a list of numbers.
unique_num = {"45", "34", "123", "58", "99"}
print(unique_num)

# 4) merge two dictionaries into one


def merge(person_1, person_2):
    res = {}
    for key in person_1.keys() | person_2.keys():
        if key in person_1 and key in person_2:
            if key == 'age':
                res[key] = [person_1[key], person_2[key]]
            else:
                res[key] = [person_1[key], person_2[key]]
        elif key in person_1:
            res[key] = person_1[key]
        else:
            res[key] = person_2[key]
    return res


person_1 = {'name': 'Melissa', 'age': '24', 'address': 'Brooklyn street 26'}
person_2 = {'name': 'John', 'age': '28', 'address': 'New York 1234'}
person_3 = merge(person_1, person_2)
print(person_3)

# 5) Implement a function that removes a key-value pair from a dictionary.
person_1 = {'name': 'Melissa', 'age': '24', 'address': 'Brooklyn street 26'}
if "address" in person_1:
    person_1.pop("address")

print(person_1)

# 6) Create a program that checks if two sets have any elements in common.
unique_num = {45, 34, 123, 58, 99}
avg_num = {22, 34, 58, 100, 145}
print(unique_num.intersection(avg_num))

# 7)Write a Python program that counts the number of occurrences
# of each character in a given string using a dictionary.


def count_characters(string):
    # Create an empty dictionary to store character counts
    char_count = {}

    # Iterate through the characters in the string
    for char in string:
        # Check if the character is already in the dictionary
        if char in char_count:
            # If it is, increment the count
            char_count[char] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            char_count[char] = 1

    return char_count


# Input string
input_string = "Regi does something every single day."

result = count_characters(input_string)

for char, count in result.items():
    print(f"'{char}': {count}")