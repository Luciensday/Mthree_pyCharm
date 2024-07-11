"""
*
**
**
*   *
"""


num = int(input("Enter odd number granter than 5:  "))


if num % 2 == 1 and num >= 5:
    totalCols = num
    totalRows = (num + 1) // 2

    for i in range(1, totalCols + 1):
        for j in range(1, totalRows + 1):
            if j == 1 or i == j or i + j == totalCols + 1:
                print("*", end="\t")
            else:
                print(end="\t")
        print()
else:
    print("number need to be greater than 5 and odd number")