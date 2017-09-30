#Zev Stravitz
#Line of best fit - least square method
#5/13/15

from Tkinter import *

print 'Welcome to the line of best fit linear grapher'
print 'f(x) = mx + b'
#Make blank list for the x and y coordinates
xlist = []
ylist = []
coordinates = ''
#Take in coordinates until they type in P
while True:
    val = raw_input("Insert a coordinate seperated by commas(Enter q when done): ")
    if val == 'q':
        break
    xval, yval = val.split(',')
    #Split the x and y and set them to their respective lists
    xlist.append(float(xval))
    ylist.append(float(yval))
xsum, ysum, counterx, countery,changex,changey = 0,0,0,0,0,0
#Find the average for x and y
for i in xlist:
    xsum = xsum + i
    counterx = counterx + 1
for i in ylist:
    ysum = ysum + i
#Use counterx for both because x and y have the same # of coordinates
avex = xsum/counterx
avey = ysum/counterx
for i in xlist:
    xA = i - avex
    changex = changex + (xA**2)
i = 0
while i <= (counterx-1):
    xA = (xlist[i]) - avex
    yA = (ylist[i]) - avey
    changey = changey + ((xA)*(yA))
    i = i + 1
m = (changey/changex)
yint = avey - (m * avex)
print 'your equation is y = ', m, 'x + ', yint

def board():
    canvas.create_line(250, 0, 250, 500, fill="red", width=5)
    canvas.create_line(0, 250, 500, 250, fill="red", width=5)
    for i in range(1,20):
        x = 25*i
        canvas.create_line(0+x, 245, 0+x, 255, fill="red", width=3)
    for i in range(-10,10):
        y = 25*i
        canvas.create_line(245, 250+y, 255, 250+y, fill="red", width=3)


def graphcoor(m,yint,xlist,ylist,counterx):
    b = yint*25
    canvas.create_line(500,250-b-(10*(m*25)), 0, 250-b+(10*(m*25)), fill="red", width=3)
    i = 0
    while i <= (counterx-1):
        xcoor = (xlist[i])
        ycoor = (ylist[i]) 
        i = i + 1
        xprint = xcoor * 25
        yprint = ycoor * 25
        canvas.create_oval(250+xprint, 250-yprint, 250+xprint, 250-yprint, fill="black", outline = 'black', width =5)
        
if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    canvas.pack()
    board()
    graphcoor(m,yint,xlist,ylist,counterx)
    root.mainloop()
