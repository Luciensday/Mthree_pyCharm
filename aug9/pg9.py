val = input("type yes or no")
print(val.casefold())
print(val.lower())
if val.casefold() == "yes":
    print("interested")
else:
    print("not interested")