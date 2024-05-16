# Write a program to find the factorial of a number using recursion.
# + make it ongoing until type exit to quit
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


run = True
while run:
    give_answer = input('Enter a number you want to find factorial value:')

    if give_answer.lower() == 'exit':
        run = False
        break

    try:
        # change the input type for integer
        give_answer = int(give_answer)
        result = factorial(give_answer)
        print(f"The factorial of {give_answer} is {result}")
    except ValueError:
        print('Invalid input! Please enter valid number or exit to quit.')

# Write a program to find the square of the largest element in an array.
