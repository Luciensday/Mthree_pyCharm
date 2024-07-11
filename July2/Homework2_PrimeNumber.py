# Prime Numbers:
# Write a program to check if a number is prime.
# Write a program to print all prime numbers between 1 and 100 using a for loop.
## prime number cannot be divide by any previous number
# 2, 3, 5, 7, 11, 13, 17, 19, 23


num = int(input("Enter a number to verify if it is a prime number: "))


if num <= 1:
    print("not a prime")
else:
    isPrime = True
    i = 2
    while i < num:
        if num % i == 0:
            isPrime = False
            break
        i += 1

    if isPrime:
        print("Yup! It's a prime")
    else:
        print("not a prime")




