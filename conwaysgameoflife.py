#Zev Stravitz
#1/9/15
#Final Project
#https://en.wikipedia.org/wiki/Conway's_Game_of_Life

from Tkinter import *

#This will create the matrix 10*10
def buildBoard():
    #Create Matrix 10X10
    M = []
    for i in range(10):
        M.append([0,0,0,0,0,0,0,0,0,0])
    return M


#This will print out the grid based on the matrix; white for 0 and black for 1
def redrawAll(M, canvas):
    #Set main coordinates
    x1 = 0
    x2 = 50
    y1 = 0
    y2 = 50
    for r in range(0,10):
       #Reset x coordinates
       x1 = 0
       x2 = 50
       for c in range(0,10):
           """Check in the matrix if the number is a one or zero
                If it's a zero, it will print out a white box, and if it's a 1
                it will print out a black box"""
           if M[r][c] == 0:
               canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline = "Black", width = 1)
           if M[r][c] == 1:
               canvas.create_rectangle(x1,y1,x2,y2,fill="black",outline = "Black", width = 1)
           x1 = x1 + 50
           x2 = x2 + 50
       #Reset Move up 50
       y1 = y1 + 50
       y2 = y2 + 50

    canvas.create_text(250, 525, text="NEXT GENERATION", fill="black", font="Times 26")

    
#This will calculate the number of neighbors so that it can 
def numNeighbors(M,r,c):
    counter = 0
    #Check left,right,up,down
    if r != 0:
        if M[r-1][c] == 1:
            counter = counter + 1
    if c != 0:    
        if M[r][c-1] == 1:
            counter = counter + 1
    if r != 9:
        if M[r+1][c] == 1:
            counter = counter + 1
    if c != 9:
        if M[r][c+1] == 1:
            counter = counter + 1
    #Check diagnally in each direction
    if r != 0 and c != 0:
        if M[r-1][c-1] == 1:
            counter = counter + 1
    if r != 0 and c != 9:          
        if M[r-1][c+1] == 1:
            counter = counter + 1
    if r != 9 and c != 0:
        if M[r+1][c-1] == 1:
            counter = counter + 1
    if r != 9 and c != 9:
        if M[r+1][c+1] == 1:
            counter = counter + 1
    return counter

#This will print the next generation when they click the botton
def nextGeneration(M):
    M2 = buildBoard()
    for r in range(0,10):
        for c in range(0,10):
            #Although a new matrix is created, the number of neighbors must stay the same or the number of neighbors will overlap
            N = numNeighbors(M,r,c)
            if M[r][c] == 1:
                if N < 2 or N > 3:
                    M2[r][c] = 0
                else:
                    M2[r][c]=1
            if M[r][c] == 0:
                if N == 3:
                    M2[r][c] = 1
    for r in range(0,10):
        for c in range(0,10):
            M[r][c] = M2[r][c]
    redrawAll(M,canvas)

#This will change the grid each time they click on a square and call the next gen. function when they click below the grid
def mouseClick(event,canvas,M):
    x = event.x
    y = event.y
    #print event.x, event.y
    a = int((10*event.y)/(500))
    #y is first because it checks the row first
    b = int((10*event.x)/(500))
 #If they click below the grid it will call nextgen
    if a >= 10:
        nextGeneration(M)
    else:
        if M[a][b] == 1:
            M[a][b] = 0
            redrawAll(M,canvas)
        else:
            M[a][b] = 1
            redrawAll(M,canvas)
            

if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=500, height=600)
    canvas.pack()
    M = buildBoard()
    redrawAll(M,canvas)
    root.bind("<Button-1>",lambda event:mouseClick(event,canvas,M))
    root.mainloop()
