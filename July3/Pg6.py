"""
n = 1234     target 4321

rev = -

n   r=n%10  rev=rev*10+r    n=n//10
------------------------------------
1234    4   =0*10+4=4      123
123     3   =4*10+3=43     12
12      2   =43*10+2=432    1
1       1   =432*10+1=4321  0

"""

n = int(input("Enter the n value = "))

rev = 0
while n > 0:
    r = n%10
    rev = rev * 10 + r
    n = n//10
print("Rev = ", rev)


'''
same as string method

reverse = n[::-1]

'''





