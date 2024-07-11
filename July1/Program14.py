# print num from 10 to 40 except multiple of 5
i = 10
while i <= 40:
    if i % 5 == 0:
        i += 1
        continue
    print(i)
    i = i + 1

