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
        
        
        
        
