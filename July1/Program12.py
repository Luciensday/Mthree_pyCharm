# "else" will only excute when all the while loop sucessfully complete

i = 1
while i <= 10:
    print(i)
    ch = input("press q to exit")
    if ch == "q":
        break
    i += 1
else:
    print("I am getting executed only if loop is not broken ")

print("this is outside while loop")


