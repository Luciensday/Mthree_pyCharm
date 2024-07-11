'''
Starting with the defined fruit_list in the code block below, update the script to perform the following tasks.

Prompt the user to enter the name of a fruit.
If the fruit is in fruit_list, display an appropriate message to the user and tell the user its index value in the list.
If the fruit is not in fruit_list, display an appropriate message to the user and prompt them to try again.
The script should repeat itself until the user enters a stop word at the prompt.
fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]

# Your code here
Tip
It's always a good idea to tell the user how to end a loop!

'''


fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]





while True:
    userInput = input("Enter a fruit to check if it's on the list, if you want to stop enter 'stop': ").strip().lower()
    if userInput == "stop":
        print("programme close")
        break
    foundfruit = False
    for i in range(len(fruit_list)):
        if fruit_list[i] == userInput:
            foundfruit = True
            print(f"Bingo! {fruit_list[i]} is on the list! The index is {i}")
            break
    if not foundfruit:
        print(f"nope! {userInput} is not on the list! try again")




