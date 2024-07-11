# Write a program to print all prime numbers between 1 and 100 using a for loop.
# 2, 3, 5, 7, 11, 13, 17, 19, 23

def is_prime(n):
    if n <= 1:
        return False
    # longer loop:  check all number smaller than n is dividable. for example 4 => need to check 2 and 3 | 5 => check 2, 3, 4
    # shorter loop: only need to check until n's square foot.  if n is 26, only need to check 2, 3, 4, 5. and then plus one to ensure cover the squarefoot itself
    for i in range(2, int(n**0.5) + 1 ):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 1 to 100 are: ")
for num in range(1, 101):
    if is_prime(num):
        print(num)


