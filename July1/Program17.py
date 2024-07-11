# list all the numbers between 100 to 200 that is multiple of 2, 3

i = 100
a = 2
b = 3
while i <= 200:
    if i % (a * b) == 0:
        print("con: ", i)
        i += (a * b)
        continue

    i += 1
