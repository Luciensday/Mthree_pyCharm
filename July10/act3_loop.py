'''Activity 3
Write a Python script that computes the length of a string without using the len() function.'''

userInput = input("Enter something and we will count the word: ").strip()

count = 0

for i in userInput:
    count += 1

print(count)