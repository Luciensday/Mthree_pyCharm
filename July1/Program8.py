"""
This is program demostrates the use of if..elif and else statement
mark > 0 < 35 ....FAIL
     >= 35 < 50 ... GRADE C
     >=50 < 70  ... GRADE B
     >=70 <= 100 ... GRADE A
less than 0 and greater than 100  ----->  marks
"""

marks = int(input("Enter the marks = "))
if marks >= 0 and marks < 35:
    print("FAIL")
elif marks >= 35 and marks < 50:
    print("GRADE C")
elif marks >= 50 and marks < 70:
    print("GRADE B")
elif marks >= 70 and marks < 100:
    print("GRADE A")
else:
    print("Invalid marks (Marks shouldd be between 0 -100)")


