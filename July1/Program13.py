# continue will go back to while conddition without execute the lines behind

i = 10
while(i <= 100):
    print(i)
    i = i + 5
    if i % 20 == 0:
        continue
    print("------------------")
    print("******************")