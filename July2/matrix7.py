'''
n =4

       *
      * *
    * * * * *
  * * * * * * *
'''

num = int(input("enter the number : "))

for i in range(1, num+1):
    print(" "*(num-i), "*"*(2*i-1))


