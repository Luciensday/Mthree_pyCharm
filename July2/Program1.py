'''
Fibonacci 1, 1, 2, 3, 5, 8
1+1=2
1+2=3
2+3=5
3+5=

----
index
1
1+1
1+1+2
1+1+2+3
1+1+2+3+4
1+1+2+3+4+5



'''


# fnc1, fnc2 = 0, 1
# index = 1
#
# if index == 1:
#     print(fnc1)
# else:
#     while index < 50:
#         print(fnc1)
#         toAdd = fnc1 + fnc2
#         fnc1 = fnc2
#         fnc2 = toAdd
#         index += 1
#
# ----
nterms = int(input("How many terms of the sequence? "))
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")

while count < nterms:
    print(n1)
    nth = n1 + n2
# this is to update values as in the fibbonaci sequence:
    n1 = n2
    n2 = nth
    count += 1