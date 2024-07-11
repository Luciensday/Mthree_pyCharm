# names = ["Robert", "Mark", "Nick", "Jenny"] # Do not change this
# print(names)
#
# nameSet = set(names)
# print(nameSet)

# names = {"Robert", "Mark", "Nick","Jenny"}
# print(names)
#
# another_set = set()
# another_set = names
# print(another_set)

# states_abbrev = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
#                  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
#                  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
#                  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
#                  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"}
#
# # Your code here
# userInput = input('enter abbreviate state: ').upper()
#
# if userInput in states_abbrev:
#     print('Success')
# else:
#     print('invalid')

# userList = set()
# def displayInput(userList):
#     for val in userList:
#         print(val)
#
# while True:
#     userInput = input("Enter stuff you want to put to the set, to quit please enter 'quit' ")
#     if userInput.lower() == "quit":
#         displayInput(userList)
#         break
#     else:
#         userList.add(userInput)


# qty_of_words = int(input("Enter the size of word bank: "))
#
# userSet = set()
#
# i = 1
#
# while i <= qty_of_words:
#     wordInput = input(f"{i}: ")
#     userSet.add(wordInput)
#     i += 1
# else:
#     for j in userSet:
#         print(j)


# food = {"pasta", "burger", "hotdog", "pizza"}
#
# # # The remove shouldn't throw an error.
# # food.remove("taco")
# def foodRemove():
#     userInput = input("enter the food name to delete:  ")
#     if userInput in food:
#         food.remove(userInput)
#         print(f"current set is: {food}")
#     else:
#         print("friendly reminder - choice wisely")
#         print(f"current set is: {food}")
# print(f"current set is: {food}")
# while True:
#     foodRemove()
#
#     if len(food) <= 0:
#         print("no food left!")
#         break

#
# #Practice 11
# food = {"pasta", "burger", "hotdog", "pizza"}
# while True:
#     print(f"currently you have {len(food)} in the set: {food}")
#     userInstruction = input("do you want to delete something? enter yes/no")
#     if userInstruction.upper() == "YES":
#         if len(food) == 0:
#             print("Oh no. nothing to delete!")
#             break
#         else:
#             popItem = food.pop()
#             print(f"You have remove {popItem}")
#     elif userInstruction.upper() == "NO":
#         print(f"bye!")
#         break
#     else:
#         print("please enter valid value")

#
# # practice 12
# shake_1 = {"banana", "blueberry", "spinach"}
# shake_2 = {"strawberry", "pistachio", "cocoa powder"}
# shake_3 = {"kiwi", "banana", "peanut butter"}
#
#
# sets = {
#     "shake_1": shake_1,
#     "shake_2": shake_2,
#     "shake_3": shake_3
# }
#
# def verifyingSet():
#     if len(sets) == 0:
#         exit()
#
# while True:
#     setskey = ", ".join(sets.keys())
#     set_name = input(f"Enter the name of the set you want to delete {setskey}: ").strip()
#
#
#
#     if set_name in sets:
#         del sets[set_name]
#         print(f"The set '{set_name} has been deleted")
#         verifyingSet()
#
#     else:
#         print(f"error   The set '{set_name}' does not exist")
#
states_abbrev = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                 "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                 "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                 "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                 "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"}

# Your code here
userSet = set()

while True:
    userInput = input("Enter a state that you have visited. when complete enter 'done' ").upper()
    if userInput in states_abbrev:
        userSet.add(userInput)
    elif userInput.lower() == "done":
        notvisited = states_abbrev.difference(userSet)
        print(f"the place that you haven't visit are: ")
        for i in notvisited:
            print(i)
    else:
        print("hmmm we don't recognise this state. try again!")


