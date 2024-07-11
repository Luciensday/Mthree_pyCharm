# Write a program to check if a number is prime.
# Write a program to print all prime numbers between 1 and 100 using a for loop.
# Factorials:


# 2, 3, 5, 7, 11, 13, 17 , 19, 23, 29



# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 4 is not prime,  attempt to divide it by 1, 2, 3   and dividable by 2
#

n = 2
prime = []

## find any prime number smaller than 50

while n < 50:
    for i in range(n):
        if n % i == 0:
            n += 1
        




