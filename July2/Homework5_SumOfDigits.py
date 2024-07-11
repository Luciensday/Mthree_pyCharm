# Sum of Digits:
# Write a program to find the sum of digits of a given number using a while loop.
# e.g. number = 12345.  result should be 1+2+3+4+5 =15


n = int(input("Enter a number to calculate a sum of all digits: "))


sumOfDigit = 0
# using while loop and %10 each time
while n > 0:
    digit = n % 10
    sumOfDigit += digit
    # prepare for the next loop
    n = n // 10

print("sum of digit is: ", sumOfDigit)