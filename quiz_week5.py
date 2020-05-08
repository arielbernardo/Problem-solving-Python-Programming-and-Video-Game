# Problem Solving, Python Programming, and Video Games
# Week 5
# Programming (elif and else clause)

# Write a Python program that asks the user to input a non-negative integer. If the user enters a non-negative integer, output two times that value. If the user does not enter a non-negative integer, output a warning message.

# For example, here are two sample program runs:

# Enter a non-negative integer >43
# 43 * 2 is 86

# Enter a non-negative integer >hello
# hello is not a non-negative integer


n = input('Enter a non-negative integer >')
try:
    val = int(n)
    if val > 0:
        print(val, '* 2 is', val*2)
    elif val < 0:
        print(val, 'is not a non-negative integer')
except ValueError:
    try:
        val = n
        print(val, 'is not a non-negative integer')
    except ValueError:
        pass
       
        
        
        
# Programming (keyword operator, short circuit evaluation, unary expression, and operator precedence)
# Write a Python program that asks the user to input an integer. If the user enters an integer, output the negative of that integer. If the user does not enter an integer, output a warning message. For this question a valid integer consists of one or more digits (0-9) with an optional leading minus sign (-).

# For example, here are three sample program runs:
# Enter an integer >-43
# The negative of -43 is 43

# Enter an integer >43
# The negative of 43 is -43Enter an integer >fortythree

# fortythree is not an integer

n = input('Enter an integer >')
try:
    val = int(n)
    if val < 0:
        print('The negative of {} is {}'.format(val, abs(val)))
    elif val > 0:
        print('The negative of {} is {}'.format(val, -abs(val)))
except ValueError:
    try:
        val = n
        print('{} is not an integer'.format(val))
    except ValueError:
        pass
