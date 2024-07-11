'''
Activity 15
Write a Python script that determines if an input number can be expressed as the sum of two prime numbers.

For example, the number 10 can be expressed as the sum of two prime numbers:

10 = 3 + 7 : both prime numbers
10 = 5 + 5 : both prime numbers
However, the number 11 cannot be:

11 = 1 + 10 : neither 1 nor 10 are prime numbers
11 = 2 + 9 : 9 is not a prime number
11 = 3 + 8 : 8 is not a prime number
11 = 4 + 7 : 4 is not a prime number
11 = 5 + 6 : 6 is not a prime number
'''

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def can_be_expressed_as_sum_of_two_primes(number):
    for i in range(2, number // 2 + 1):
        if is_prime(i) and is_prime(number - i):
            print(f"{number} = {i} + {number - i}")
            return True
    return False

# Input from the user
number = int(input("Enter a number: "))

# Check if the number can be expressed as the sum of two prime numbers
if not can_be_expressed_as_sum_of_two_primes(number):
    print(f"{number} cannot be expressed as the sum of two prime numbers.")

#
# userInput = int(input("Enter a number to varify if it can be express as the sum of two prime number: "))
#
# # 10 => 9    the other one is userinput(10 - i ). verify if it's prime
#
#
#
# def primeChecker(n):
#     for i in range(2, n-1):
#         if n % i == 0:
#             return False
#         else:
#             return True
#     #if it's 5, check 2,3,4
#
# for j in range(1,userInput):
#     otherNumber = userInput - j
#     if primeChecker(j) or primeChecker(otherNumber):
#         print(f'the number {userInput} can be divide by two prime numbers {j} and {otherNumber}')
#     else:
#         print(f"false - the {userInput} is dividable by some non-prime numbers")
