'''
Activity 12
Write a script that calculates the greatest common denominator between two numbers.

For example, given the numbers 18 and 27, the greatest common denominator is 9.
'''
print("This is to calculate Greatest common denominator by two numbers ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1GCD = []
for i in range(2, num1):
    if num1 % i == 0:
        num1GCD.append(i)
print(num1GCD)

num2GCD = []
for i in range(2, num2):
    if num2 % i == 0:
        num2GCD.append(i)
print(num2GCD)

intersectionSet = set(num1GCD) & set(num2GCD)

if intersectionSet:
    commonGCD = max(intersectionSet)
    print(commonGCD)
else:
    print(f"{num1} & {num2} has no common demoninator")