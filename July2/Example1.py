'''
n = number of records you want to enter
name, roll, ,arks
append in the list
function and loops
'''
def insertRecord():
    name = input("Enter the name = ")
    roll = input("Enter the roll = ")
    marks = input("Enter the marks = ")
    return [name, roll, marks]

records = []
while True:
    ch = int(input("1 Insert a record 2 Display records 3 Exit"))
    if ch == 1:
        rec = insertRecord()
        records.append(rec)
    elif ch == 2:
        print("-"*50)
        print("RECORDS".center(50))
        print("-"*50)
        for x in records:
            print("NAME = ", x[0], end="\t")
            print("ROLL = ", x[1], end="\t")
            print("ROLL = ", x[2] )
    elif ch == 3:
        print("PROGRAM END".center(50,"*"))
        break

    else:
        print("invalid choice ")
