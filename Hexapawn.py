#Zev Stravitz and Michael Weinberger
#Spring 2016
#Machine-learning program where computer improves at playing hexapawn
#https://en.wikipedia.org/wiki/Hexapawn

from copy import deepcopy
import random

class Tree:

    def __init__(self,element=None,parent=None,children=None): #Constuctor for Tree
        self.element = deepcopy(element)
        self.parent = parent
        self.children = []

    def __len__(self): #Length function for tree - Calculates number of nodes
        if self.element == None:
            return 0
        elif len(self.children) == 0:
            return 1
        total = 1
        for child in self.children:
            total += len(child)
        return total

    def makeTree(self,counter=1): #This goes through all of the possible moves of the tree and adds them to the tree.
        M = deepcopy(self.element)
        r = len(self.element)
        c = len(self.element[0])
        for i in range(0,r):
            for j in range(0,c):
                if counter%2 != 0 and self.element[i][j] == 1:
                        if legalmoveComp(self.element,i-1,j,i,j,counter):
                            copy = deepcopy(self.element)
                            copy[i-1][j] = copy[i][j]
                            copy[i][j] = 0
                            new = Tree(element=copy,parent=self)
                            self.children.append(new)
                            if WinnerCheck(copy,r,c,counter) == 0:
                                Tree.makeTree(self.children[-1],counter+1)
                        if legalmoveComp(self.element,i-1,j-1,i,j,counter):
                            copy = deepcopy(self.element)
                            copy[i-1][j-1] = copy[i][j]
                            copy[i][j] = 0
                            new = Tree(element=copy,parent=self)
                            self.children.append(new)
                            if WinnerCheck(copy,r,c,counter) == 0:
                                Tree.makeTree(self.children[-1],counter+1)
                        if legalmoveComp(self.element,i-1,j+1,i,j,counter):
                            copy = deepcopy(self.element)
                            copy[i-1][j+1] = copy[i][j]
                            copy[i][j] = 0
                            new = Tree(element=copy,parent=self)
                            self.children.append(new)
                            if WinnerCheck(copy,r,c,counter) == 0:
                                Tree.makeTree(self.children[-1],counter+1)
                elif counter%2 == 0 and self.element[i][j] == 2:
                        if legalmoveComp(self.element,i+1,j,i,j,counter):
                            copy = deepcopy(self.element)
                            copy[i+1][j] = copy[i][j]
                            copy[i][j] = 0
                            new = Tree(element=copy,parent=self)
                            self.children.append(new)
                            if WinnerCheck(copy,r,c,counter) == 0:
                                Tree.makeTree(self.children[-1],counter+1)
                        if legalmoveComp(self.element,i+1,j+1,i,j,counter):
                            copy = deepcopy(self.element)
                            copy[i+1][j+1] = copy[i][j]
                            copy[i][j] = 0
                            new = Tree(element=copy,parent=self)
                            self.children.append(new)
                            if WinnerCheck(copy,r,c,counter) == 0:
                                Tree.makeTree(self.children[-1],counter+1)
                        if legalmoveComp(self.element,i+1,j-1,i,j,counter):
                            copy = deepcopy(self.element)
                            copy[i+1][j-1] = copy[i][j]
                            copy[i][j] = 0
                            new = Tree(element=copy,parent=self)
                            self.children.append(new)
                            if WinnerCheck(copy,r,c,counter) == 0:
                                Tree.makeTree(self.children[-1],counter+1)

    def findChild(self,board): #Function to find the node of a board
        for child in self.children:
            if child.element == board:
                return child
        
    def Treechoose(self,counter): #Function that randomly chooses a move for the tree
        spot = random.randint(0,len(self.children)-1)
        return self.children[spot]

    def treeTrimmer(self,ComputerMoves):
        x = -1
        p = ComputerMoves[-1].parent
        if p == None:
            self.children = []
            return
        while len(p.children)<=1:
            if p.parent != None:
                if p.parent.parent != None:
                    p = p.parent.parent
                    x -= 1
                else:
                    self.children = []
                    return
            else:
                self.children = []
                return
        p.children.remove(ComputerMoves[x])

def legalmoveComp(M,movey,movex,spoty,spotx,counter):
    r = len(M) - 1
    c = len(M[0]) - 1
    if movex > c or movey > r or movex < 0 or movey < 0:
        return False
    if counter%2 != 0: #If it is odd
        if spoty - movey == 1 and abs(spotx-movex) <= 1:
            if spotx == movex and spoty == movey + 1: #If it is moving up for player 1
                if M[movey][movex] == 0:
                    return True
                else:
                    return False
            elif spotx == movex + 1 or spotx == movex - 1 and spoty == movey + 1: #If it is moving diagnolly up right or left
                if M[movey][movex] == 2:
                    return True
                else:
                    return False
    elif counter%2 == 0: #If it is even.
        if movey - spoty == 1 and abs(movex-spotx) <= 1: #If it is a legal move
            if spotx == movex and spoty == movey - 1: #If it is move up for player 2
                if M[movey][movex] == 0:
                    return True
                else:
                    return False
            elif spotx == movex + 1 or spotx == movex - 1 and spoty == movey - 1: #If it is moving diagnolly down left or right
                if M[movey][movex] == 1:
                    return True
                else:
                    return False

def legalmove(M,movex,movey,spotx,spoty,counter):
    r = len(M)
    c = len(M[0])
    if movex > c-1 or movey > r-1 or movex < 0 or movey < 0:
        print  "Row or column is out of range."
        return False
    if counter%2 != 0: #If it player one's turn
        if spoty - movey == 1 and abs(spotx-movex) <= 1:
            if spotx == movex and spoty == movey + 1: #If it is moving up for player 1
                if M[movey][movex] != 0:
                    print "That is an illegal move."
                    return False
                elif M[movey][movex] == 0:
                    return True
            elif spotx == movex + 1 or spotx == movex - 1 and spoty == movey + 1: #If it is moving diagnolly up right or left
                if M[movey][movex] != 2:
                    print 'That is an illegal move.'
                    return False
                elif M[movey][movex] == 2:
                    return True
    else: #If it is player two's turn.
        if movey - spoty == 1 and abs(movex-spotx) <= 1: #If it is a legal move
            if spotx == movex and spoty == movey - 1: #If it is move up for player 2
                if M[movey][movex] != 0:
                    print "That is an illegal move."
                    return False
                elif M[movey][movex] == 0:
                    return True
            elif spotx == movex + 1 or spotx == movex - 1 and spoty == movey - 1: #If it is moving diagnolly down left or right
                if M[movey][movex] != 1:
                    print "That is an illegal move."
                    return False
                elif M[movey][movex] == 1:
                    return True

def buildBoard(r,c,M):
    M.append(c*[2])
    for i in range(r-2):
        M.append(c*[0])
    M.append(c*[1])
    return M

def askUserSpot(counter):
    r = len(M)
    c = len(M[0])
    if counter%2 != 0:
        player = 1
    else:
        player = 2
    spot = raw_input("Player" + " " + str(player) + ": " + "Insert a coordinate for the piece you want to move (column,row): ")
    spotx, spoty = spot.split(',')
    spotx, spoty = int(spotx), int(spoty)
    spotx, spoty = spotx - 1, spoty - 1
    if spotx > c-1 or spoty > r-1 or spotx < 0 or spoty < 0:
        print 'Row or column is out of range.'
        return askUserSpot(counter)
    if counter%2 != 0:
        if M[spoty][spotx] != 1:
            print "That is not your piece."
            return askUserSpot(counter)
    elif counter%2 == 0:
        if M[spoty][spotx] != 2:
            print 'That is not your piece.'
            return askUserSpot(counter)
    askUserMove(counter,spotx,spoty)

def askUserMove(counter,spotx,spoty):
    move = raw_input("To where do you want to move (column,row)? \nType in q,q if you want to change your spot: ")
    movex, movey = move.split(',')
    if movex == "q" and movey == "q":
        askUserSpot(counter)
    else:
        movex, movey = int(movex), int(movey)
        movex, movey = movex - 1, movey - 1
    if legalmove(M,movex,movey,spotx,spoty,counter) == True:
        if counter%2 != 0:
            M[movey][movex] = 1
            M[spoty][spotx] = 0
        else:
            M[movey][movex] = 2
            M[spoty][spotx] = 0
    else:
        return askUserMove(counter,spotx,spoty) 

def WinnerCheck(M,r,c,counter): #This function runs AFTER the player makes a move. Note: Counter has not changed, if player 1 went, counter is still equal to 1.
    if counter%2 != 0: #If it is player one's turn. This checks if there are any 1's on 2's side.
        Stalematefor2 = True
        totalpieces2 = 0
        for i in range(r):
            for k in range(c):
                if M[i][k] == 2:
                    totalpieces2 += 1
        if totalpieces2 == 0:
            return 1
        for i in range(c):
            if M[0][i] == 1:
                return 1
        for y in range(r): #For each row
            for x in range(c): #For each column
                if M[y][x] == 2: #If the spot has a 2 in it
                    if x == 0:
                        if M[y+1][x] == 0 or M[y+1][x+1] == 1:
                            Stalematefor2 = False
                    elif x == c-1:
                        if M[y+1][x] == 0 or M[y+1][x-1] == 1:
                            Stalematefor2 = False
                    else:
                        if M[y+1][x] == 0 or M[y+1][x-1] == 1 or M[y+1][x+1] == 1:
                            Stalematefor2 = False
        if Stalematefor2 == True:
            return 1
    elif counter%2 == 0: #If it is player two's turn. This checks if there are any 2's on 1's side.
        Stalematefor1 = True
        totalpieces1 = 0
        for i in range(r):
            for k in range(c):
                if M[i][k] == 1:
                    totalpieces1 += 1
        if totalpieces1 == 0:
            return 2
        for i in range(c):
            if M[r-1][i] == 2:
                return 2
        for y in range(r): #For each row
            for x in range(c): #For each column
                if M[y][x] == 1: #If the spot has a 1 in it
                    if x == 0:
                        if M[y-1][x] == 0 or M[y-1][x+1] == 2:
                            Stalematefor1 = False
                    elif x == c-1:
                        if M[y-1][x] == 0 or M[y-1][x-1] == 2:
                            Stalematefor1 = False
                    else:
                        if M[y-1][x] == 0 or M[y-1][x-1] == 2 or M[y-1][x+1] == 2:
                            Stalematefor1 = False             
        if Stalematefor1 == True:
            return 2
    return 0

def printBoard(r,c,M):
    top = " "
    for i in range(c):
        top = top + "   " + str(i+1)
    print top
    top = "  "
    for i in range(c):
        top = top + ' ---'
    print top
    for j in range(r):
        board = str(j+1)
        lines = "  "
        for k in range(c):
            board = board + " | " + str(M[j][k])
            lines = lines + ' ---'
        board = board + " |"    
        print board
        print lines

if __name__ == '__main__':
    Ans = raw_input("1. Player vs. Player \n2. Player vs. Computer \n3. Computer vs. Computer \nPick a number: ")
    r = int(raw_input("Rows (at least 3): "))
    c = int(raw_input("Columns (at least 3): "))
    counter = 1
    M = []
    buildBoard(r,c,M)
    W = 0
    if Ans == "2":
        T = Tree(element=M)
        T.makeTree()
    if Ans == "3":
        T1 = Tree(element=M)
        T1.makeTree()
        T2 = Tree(element=M)
        T2.makeTree()
    games1 = 0
    games2 = 0
    again = True
    while again == True:
        if Ans == "2":
            current = T
            ComputerMoves = []
        if Ans == "3":
            current1 = T1
            current2 = T2
            Computer1Moves = []
            Computer2Moves = []
        if Ans != "3":
            printBoard(r,c,M)
        while W == 0:
            if Ans == "1": #If it is player vs player
                askUserSpot(counter)
                printBoard(r,c,M)
            elif Ans == "2": #If it is computer vs player
                if counter%2 != 0: #If it is player one's turn
                    askUserSpot(counter)
                    if current != None:
                        current = current.findChild(M)
                else:
                    if current != None:
                        current = current.Treechoose(counter)
                        M = deepcopy(current.element)
                        ComputerMoves.append(current)
                        print "The Computer is thinking...It makes its move. "
                printBoard(r,c,M)
            elif Ans == "3":
                if counter%2 != 0:
                    if current1 != None:
                        current1 = current1.Treechoose(counter)
                        current2 = current2.findChild(current1.element)
                        M = deepcopy(current1.element)
                        Computer1Moves.append(current1)
                else:
                    if current1 != None:
                        current2 = current2.Treechoose(counter)
                        current1 = current1.findChild(current2.element)
                        M = deepcopy(current1.element)
                        Computer2Moves.append(current2)
                #printBoard(r,c,M)
            W = WinnerCheck(M,r,c,counter)
            counter += 1
        if Ans == "2":
            if W == 1:
                if current != None:
                    T.treeTrimmer(ComputerMoves)
        if Ans == "3":
            if W == 1:
                T2.treeTrimmer(Computer2Moves)
            elif W == 2:
                T1.treeTrimmer(Computer1Moves)
        if W == 1:
            print "--------------- GAMEOVER ---------------  \nPlayer 1 won."
            games1 += 1
        elif W == 2:
            print "--------------- GAMEOVER ---------------  \nPlayer 2 won."
            games2 += 1
        W = 0
        M = []
        buildBoard(r,c,M)
        counter = 1
        if Ans == "1":
            Player1 = "Player 1"
            Player2 = "Player 2"
        elif Ans == "2":
            Player1 = "Player 1"
            Player2 = "Computer"
        elif Ans == "3":
            Player1 = "Computer 1"
            Player2 = "Computer 2"
            again = True
        print Player1,"wins = ", games1
        print Player2,"wins = ", games2
        if Ans == "1" or Ans == "2":
            playagain = raw_input("Do you want to play again? (Y/N) ")
            if playagain == "Y":
                again = True
            else:
                again = False
        if Ans == "3":
            if len(T1.children) == 0:
                again = False
                print "Computer 1 resigns. Computer 2 wins."
            elif len(T2.children) == 0:
                again = False
                print "Computer 2 resigns. Computer 1 wins."
