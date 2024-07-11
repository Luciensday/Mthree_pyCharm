# Palindrome:
# Write a program to check if a given string is a palindrome.
# A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# e.g. "racecar "level" "A man, a plan, a canal, Panama" "121"

userStr = input("Enter a phrase or number to check if it is palindrome: ")


if userStr == userStr[::-1]:
    print("Yup! It's palindrome")
else:
    print("Nope - not a palindrome ")
