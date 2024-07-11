'''
Write a program that performs the following steps:

Start with a street address that includes a building/house number, the name of the street, and the type of street (e.g., Street, Avenue, Boulevard, etc.).
You can use any address you wish and abbreviations are acceptable.
An example is 25 Main Street.
Display the full address to the user.
Display the house number only in a phrase like, "The building or house number is 25."
Display the street name in a phrase like, "The street name is Main Street."
'''

s = "25 Main Street"
l = s.split(" ")
print(l)
hno = l[0]
streetName = " ".join(l[1:])
print(f"The building or house number is {hno} and street name is {streetName}")
