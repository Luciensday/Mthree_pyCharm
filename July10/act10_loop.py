'''
Activity 10
Write a script that asks the user for an integer value
 and then displays the multiplication table of that input
  number from 1 through the integer squared.
'''


userInput = int(input("Enter interger for multiplication table: "))

for i in range(1, userInput ** 2 + 1):
    multiplyResult= i * userInput
    userInputStr = str(userInput)
    indexStr = str(i)
    multiplyResultStr = str(multiplyResult)
    print(f"{userInputStr} * {indexStr} = {multiplyResultStr}")

