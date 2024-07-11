'''
Create a computer program that completes the following tasks:

It prompts the user for a series of 5 integers.
The user must be prompted for 5 numbers.
After the fifth entry, the program stops prompting for values and performs the following calculations:
the product of the integers
the average of the integers
the sum of the integers
After performing the calculations, the program should display the following to the user:
the values the user entered
each of the calculations, using a phrase that identifies the value

'''
prod = 1
l=[]
for i in range(5):
    val = int(input("Enter the input = "))
    l.append(val)
    prod = prod*val

total = sum(l)
print("\nSum of all values = ",total)
print("\nProduct of all the value - ",prod)
print("\nAverage = ", total/5)
