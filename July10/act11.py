'''
Activity 11
Create a script that identifies all prime numbers between 0 and 100.


'''



userInput = int(input("Enter a number to varify if its prime: "))

notPrime = False



for i in range(2, userInput):
    if userInput % i == 0:
        notPrime = True


if not notPrime:
    print(f"yes, {userInput} is a prime")
else:
    print(f"nope, {userInput} is not a prime")

