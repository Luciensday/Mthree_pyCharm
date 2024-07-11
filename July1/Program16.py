
#
# print all numbers between 1 to 100 which is the multiple of 4, 5 , 8


i = 1
while i <= 100:
    print(i)
    if i % 4 == 0 and i % 5 == 0 and i % 8 == 0:
        print("con", i)
        i = i + 40
    else:
       i += 1


