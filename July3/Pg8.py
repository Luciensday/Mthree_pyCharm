'''
n = 1234567
7
5
3
1

n=123456


n           r=n%10       n=n//100

1234567     7              12345
12345       5              123
123         3              1
1           1              0
'''

n = int(input("Enter a number to get the even digit"))

while n > 0:
    r = n %10
    print(r)
    n = n//100




