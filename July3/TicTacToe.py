l=[0]*9

def display():
    for i in range(len(l)):
        if i%3==0: #for every 0th 3rd 6th index we go to the next line while displaying
            print()
        print(l[i],end="\t\t")
    print()
def checkWinner(sym):
    #winning indices combination
    # horizontal 0,1,2   3,4,5    6,7,8
    #verticle 0,3,6   1,4,7   2,5,8
    #diagonal 0,4,8  2,4,6
    if ((l[0]==sym and l[1]==sym and l[2] ==sym) or
        (l[3] == sym and l[4] == sym and l[5] == sym) or
        (l[6] == sym and l[7] == sym and l[8] == sym) or
        (l[0] == sym and l[3] == sym and l[6] == sym) or
        (l[1]==sym and l[4]==sym and l[7] ==sym) or
        (l[2] == sym and l[5] == sym and l[8] == sym) or
        (l[0] == sym and l[4] == sym and l[8] == sym) or
        (l[2] == sym and l[4] == sym and l[6] == sym)):
        return True
    else:
        return False

display()
moves=1
while moves<=9:  #total 9 moves
    if moves%2==1:   #every odd move is done by player 1 alternatively
        print("Player 1 its your move")
        pos=int(input("Enter the position = "))
        # if the index/pos the user given points to 0 only then it is a valid pos
        #else you need to ask the player to re enter the valid position and it happens
        #many times in some cases hence we go for while loop rather than if statemnet
        while l[pos]!=0:
            pos=int(input("Re- Enter the position = "))
        l[pos]=1  #once you get valid pos ex 5 l[5] will be filled with 1:Player 1 symbol
        res = checkWinner(1)  #if the function returns true he is the winner
        if res==True:
            print("Player 1 won the game")
            display()
            break  #after we know who is the winner : stop the game
    else: #every even move is done by player 1 alternatively
        print("Player 2 its your move")
        pos=int(input("Enter the position = "))
        while l[pos]!=0:
            pos=int(input("Re- Enter the position = "))
        l[pos] = 2
        res=checkWinner(2)
        if res==True:
            print("Player 2 won the game")
            display()
            break
    display()
    moves=moves+1 #every time a player choses position its considered as a move so increment
else:
    print("Match draw!!!!")