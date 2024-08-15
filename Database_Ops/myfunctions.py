def inputData():
    name = input("enter the name = ")
    roll = input("Enter the roll number")
    age = input("Enter the age = ")
    return name, roll, age


def display(name, roll, age):
    print("-"*50)
    print("Name".ljust(20),name)
    print("Roll".ljust(20),roll)
    print("Age".ljust(20), age)

def add(a,b,c=0):
    return a+b+c
def sub(a,b,c=0):
    return a-b-c