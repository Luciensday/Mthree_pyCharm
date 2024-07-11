'''
 row = 2
 colums = 3
 * * *
 * * *
'''

rows = int(input("Enter the rows: "))
cols = int(input("Enter the cols: "))


for i in range(1, rows + 1 ):
    for j in range(1, cols + 1):
        print("*", end="\t")
    print()
