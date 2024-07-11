#function definition with parameter and without redturn type
def add():
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    sum = a + b
    print(sum)
#function call
add()
print("--------")
print("--------")
print("--------")
print("--------")
print("--------")
add()

#function with parameters
def calculate(x,y):
    print("Sum= ", x+y)
    print("Diff= ", x-y)
    print("Prod= ", x*y)
    print("Quot= ", x/y)

calculate(11,22)

#function with return statement
def welcome(name):
    return "Hi "+name+" welcome to the future"

res = welcome("Alex")
print(res)

#return more than 1 value
def setDetails():
    name = input("Enter the name = ")
    sub = input("Enter the subject = ")
    marks = input("Enter the marks = ")
    return name, sub, marks

# print(setDetails())  => this will only return as tuple

n, s, m = setDetails()
print(n, s, m)

# function with default parameters
def add(a,b,c=0,d=0):
    return a+b+c+d
print(add(11,22))
print(add(11,22, 45))
print(add(11,22, 45, 11))


#name arguments
def myfunc(name, roll):
    print(name)
    print(roll)

myfunc("Shilpa", 111)
myfunc(roll=99, name="Shruthi")

##multiple arg

def myfun(*args):
    print(args)

myfun(11,22,33)
myfun(10,20)
myfun(1,2,3,4,5,)

# key value paris => keyword arg
def myfun3(**kwargs):
    print(kwargs)

myfun3(name="Shilpa", ssl="1000")
myfun3(name="Alex", roll=11, sub="python")