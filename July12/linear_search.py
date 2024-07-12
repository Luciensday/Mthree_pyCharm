'''
get a list from user
ask user to enter key: 14
search in the list where the element in present and display the key in present in index =2

| 0  | 1  | 2 | 3  |
| 11 | 23 | 14 | 16 |

n = len(l) => 4

for i in range(n)
    if l[i] ==key:
        print("Found the key at index", i)
        break
else:
    print(" ")

i   l[i]
--------
0   11  11==14? F
1   23  23==14? F
2   14  14==14? T

'''

l =[11,2,33,11,24, 55,11,77]

searchkey = int(input("Enter the search key = "))
flag = 0
noOfElement = len(l)
for i in range(noOfElement):
    if l[i] == searchkey:
        flag = 1
        print("We found the key ",i)

if flag == 0:
    print("the search key {0) Not found".format(searchkey))
