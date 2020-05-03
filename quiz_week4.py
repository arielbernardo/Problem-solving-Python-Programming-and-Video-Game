# Programming (multi-argument function call)

# Write a Python program that asks the user to input two numbers and finds the max of those number when they are raised to the power of each other.

# Display three numbers in your answer, the first number raised to the power of the second, the second number raised to the power of the first, and then the maximum of these two computed values, each on one line.

# For example, here is a sample program run:

# Enter an integer >2
# Enter an integer >3
# 2 to the power of 3 is 8
# 3 to the power of 2 is 9
# the max of 8 and 9 is 9




num1 = int(input('Enter an integer >'))
num2 = int(input('Enter an integer >'))
pow_num1 = num1**num2
pow_num2 = num2**num1
max_num = pow_num1, pow_num2
print('{} to the power of {} is {}'.format(num1, num2, pow_num1))
print('{} to the power of {} is {}'.format(num2, num1, pow_num2))
print('the max of {} and {} is {}'.format(pow_num1, pow_num2, max(max_num)))


#Programming (method call and attribute reference)

#Write a Python program that asks the user to input a string and a sub-string and outputs the number of occurrences of the sub-string in the string.

#For example, here is a sample program run:

#Enter a string >banana
#Enter a substring >na
#the substring "na" appears 2 times in "banana"


user_input1 = input('Enter a string >')
user_input2 = input('Enter a substring >')
result = user_input1.count(user_input2)
print('the substring "{}" appears {} times in "{}"'.format(user_input2,result,user_input1))







