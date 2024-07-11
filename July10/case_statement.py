ch = int(input("Choose a number between 1-4: "))
match ch:
    case 1:
        print("You will have a good day ")
    case 2:
        print("You will have an average day")
    case 3:
        print("You will have a bad day")
    case 4:
        print("Do not step out")
    case _:
        print("Invalid choice ")