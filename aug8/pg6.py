i = 0
val = int(input("Enter any val = "))
while i < 10:
    if i ==val:
        break

    print(i, end="\t")
    i += 1
else:
    print("\nthis will be printing if while doesn't have break sttatement ")
