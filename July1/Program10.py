a = int(input("Enter a = "))
b = int(input("Enter b = "))
c = int(input("Enter c = "))

# nested if else condition to find max of 3 nums
if a > b:
    if a > c:
        print(a, "= max")
    else:
        print(c, "= max")
else:
    if b > c:
        print(b, "= max")
    else:
        print(c, "= max")