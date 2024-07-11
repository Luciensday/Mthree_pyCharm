# Factorials:
# Write a program to find the factorial of a number using a for loop.
'''
The factorial of a non-negative integer n, denoted as n!. is the product of all positive integers less than or equal to
n. e.g. 5! = 1*2* 3* 4 *5 = 120
'''

n = int(input("Enter a number to calculate factorials result: "))

if n < 0:
    print("Factorial is not defined for negative numbers")

result = 1
for i in range(1, n + 1):
    result *= i
print("Factorial result is: ", result)
