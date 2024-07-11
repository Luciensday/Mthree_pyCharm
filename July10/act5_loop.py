'''
Activity 5
Write two scripts, each of which displays all numbers divisible by 50 between 100 and 1000 (inclusive).

Use the range function with for in one script.
Use while without range in the other script.
Both scripts should have identical outputs.


'''
print("Using range")

for i in range(100, 1000, 50):
    print(i)

print("---------------")
print("Using While")

j = 100
while j <= 1000:
    if j % 50 == 0:
        print(j)
        j += 1
    else:
        j += 1
        continue

