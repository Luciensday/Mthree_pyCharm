# Armstrong Number:
# Write a program to check if a number is an Armstrong number.
# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example:
# 153 is an Armstrong number because 1**3 + 5**3 + 3**3= 1+125+27 =153

n = int(input("Enter a number to check if it is an Armstrong number: "))

# calculate number of digit
number = n
numDigits = 0
while number > 0:
    numDigits += 1
    number = number // 10


# calculate sum of power
number = n
sumOfPowers = 0
while number > 0:
    digit = number % 10
    sumOfPowers += digit ** numDigits
    number = number // 10


if sumOfPowers == n:
    print("Yup! it's Armstrong Number")
else:
    print("Nope!  not an Armstrong Number")