'''
number triangular
      1          =>x x x 4 x x x
     2 2         =>x x 3 x 5 x x
    3 3 3        =>x 2 x 4 x 6 x
   4 4 4 4       =>1 x 3 x 5 x 7


In  case of n=4 there should be 7 columns
n=5 should have 9 columns

n should be produce n*2-1 columns

'''

n = 5

for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end="")
    for j in range(0, i+1):
        print(i,"", end="")
    print()