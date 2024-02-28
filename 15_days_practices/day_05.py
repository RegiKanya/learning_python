# learning day 5 - STRING MANIPULATION

# 1) Given a list of words, concatenate them into a single string separated by spaces.
words_2 = ["Are", "you", "ready", "for", "this", "?"]
sencente = " ".join(words_2)
print(sencente)

# 2) Create a function to reverse a given string.
string = input("what words do you wanna reverse?")
# print(string)
reversed = string[::-1]
print(f"reverse: {reversed}")

# 3) Write a program that takes a sentence as input and counts the number of words in it.
a = input("Write a sencente: ")
count_a = len(a.split())
print(f"words in the senctence: {count_a}")

# 4) Given a string, write a function to remove all vowels from it and return the modified string.
s = input("Give me a word:")


def remove_vowels(s):
    vowels = ["a", "e", "u", "i", "o"]
    result = ""

    for i in s:
        if i not in vowels:
            result += i
    result = "".join(result)
    print(result)

    # result = [letter for letter in s if letter.lower() not in vowels]

    # result = ''.join(result)
    # print(result)


remove_vowels(s)

# 5) Write a Python program to find the length of the longest word in a sentence.
t = ["this", "is", "very-very", "long"]


def find_longest(t):
    max = len(t[0])
    temp = t[0]

    for i in t:
        if len(i) > max:
            max = len(i)
            temp = i
    print("This word is the longest:", temp)


find_longest(t)

# 6) Given a list of names, count the number of names that start with a vowel.
names = ["anna", "béla", "dávid", "ernő", "tamás"]


def count_names(names):
    vowels = ["a", "e", "u", "i", "o"]
    new_names = []

    for name in names:
        if name[0].lower() in vowels:
            new_names.append(name)
    print("this starts with vowels:", new_names)


count_names(names)

# 7) Write a function to remove all duplicate characters from a given string.
a_string = input("write a word: ")


def remove_duplicate(a_string):
    b_string = ""

    for i in a_string:
        if i not in b_string:
            b_string = b_string + i
    print(b_string)


remove_duplicate(a_string)

# ----------------
spam = "Spam, " * 4 + "beans and spams"
print(spam)
