# def myfunction():
#     print("the message prints here")
#
# myfunction()
# print("-----------")
# myfunction()


# def myfunction(name,sub):
#     print("the message prints here")
#     print(f"NAME = {name} Sub = {sub}")
#
# myfunction("Shilpa", "Python")
# print("-----------")
# myfunction("Vikas", "RDBMS")



# def takeInputs():
#     name=input("Enter the name= ")
#     age = input("Enter the age =")
#     gender = input("Enter the gender = ")
#     return name, age, gender
# mydata = takeInputs()
# print(mydata)
# n,a,g = takeInputs()
# print(f"Name = {n}")
# print(takeInputs())

#
# def add(a,b,c=10, d=0):
#     print("sum = ", a+b+c+d)
#
# add(11,22)
# add(1, 2, 3)
# add(44, 55, 6, 1)


# myfun(name,age):
# print("NAME = ",name)
# print("AGE = ",age)
#
# myfun("Derek", 44)
# myfun(age=33, name="Sharon")


# def myfun(*args):
#     for x in args:
#         print(x)
#     else:
#         print("-----------")
# myfun(11,22,33)
# myfun("shilpa","python")
# myfun(1,2,3,4,)


def myfun(**kwargs):
    for key,val in kwargs.items():
        print(f"{key} === {val}")

myfun(name="Shilpa", age="88")
myfun(roll=11, sname="amit", fee=999)