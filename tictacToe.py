#z#zev
#4/23/15
#12/3/15

from Tkinter import *
import random

#This will create the matrix 10*10
def buildBoard():
    #Create Matrix 10X10
    M = []
    for i in range(3):
        M.append([0,0,0])
    return M

#This will print out the grid based on the matrix; white for 0 and black for 1
def redrawAll(M, canvas):
    #Set main coordinates
    x1 = 0
    x2 = 100
    y1 = 0
    y2 = 100
    for r in range(0,3):
       #Reset x coordinates
       x1 = 0
       x2 = 100
       for c in range(0,3):
           """Check in the matrix if the number is a one or zero
                If it's a zero, it will print out a white box, and if it's a 1
                it will print out a black box"""
           if M[r][c] == 0:
               canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline = "Black", width = 1)
           if M[r][c] == 1:
               canvas.create_line(x1, y1, x2, y2, fill="red", width=5)
               canvas.create_line(x1, y2, x2, y1, fill="red", width=5)
           if M[r][c] == 2:
               canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline = "Black", width = 1)
               canvas.create_oval(x1,y1,x2,y2, fill="blue")
           x1 = x1 + 100
           x2 = x2 + 100
       #Reset Move up 50
       y1 = y1 + 100
       y2 = y2 + 100
       
def mouseClick(event,canvas,M):
    x = event.x
    y = event.y
    #print event.x, event.y
    a = int((3*event.y)/(300))
    #y is first because it checks the row first
    b = int((3*event.x)/(300))
##    print a
##    print b
    if M[a][b] == 0:
        M[a][b] = 1
    elif M[a][b] == 1:
        M[a][b] = 2
    elif M[a][b] == 2:
        M[a][b] = 0
    redrawAll(M,canvas)
            
if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()
    M = buildBoard()
    redrawAll(M,canvas)
    root.bind("<Button-1>",lambda event:mouseClick(event,canvas,M))
    root.mainloop()
