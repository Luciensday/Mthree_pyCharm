'''
Activity 7
Create a script that computes the factorial of any number input by the user.
'''

userInput = int(input("Enter a number for factorial result: "))

result = 1
for i in range(1, userInput+1):
    result *= i

print(result)