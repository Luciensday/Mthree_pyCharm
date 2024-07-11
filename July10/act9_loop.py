'''
Create a script that asks the user for a variable
number of values and displays the sum of those values to
 the user. The program should prompt the user for values
 until the user enters the word "quit" (uppercase or lowercase),
  display the values used in the calculation, and then display
  the total of those values.
'''

print("if you want to stop the programme any time. please enter 'quite'")

totalsum = 0
values = []

while True:
    userInput = input("Please enter number to add: ").strip().lower()

    if userInput == "stop":
        valueDisplay = " + ".join(values)
        print(f"{valueDisplay} = {totalsum}")
    try:
        inputInValueForm = int(userInput)
    except ValueError:
        print("please enter a valid number")
        continue

    totalsum += inputInValueForm
    values.append(str(inputInValueForm))

'''
ValueError
ValueError is a specific type of exception in Python.
 It occurs when a function receives an argument of the 
 correct type but inappropriate value. In the context 
 of your code, a ValueError will be raised if the user 
 inputs a string that cannot be converted to an integer
  using int().'''
