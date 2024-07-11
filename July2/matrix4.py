'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''

n = 5
for rows in range(n, 0, -1):
    for cols in range(n, rows-1, -1):
        print(cols, end="\t")
    print()