"""create a multiplication table using nested for loop
num = 5
5*1 = 5
5*2 = 10
5*3= 14
...

"""

num = int(input("Enter a number: "))
for i in range(1,11):
    print(num,"*", i,"=",num*i)