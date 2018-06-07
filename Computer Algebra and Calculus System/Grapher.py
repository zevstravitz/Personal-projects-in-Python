#Zev Stravitz
#9/27/15
import math
from Tkinter import *

print 'Welcome to the derivative calculator/grapher for all functions'
print 'Type in your function as thus: \nMultiplication symbol: *\n Exponent symbol: **\n Addition symbol: +\n Subtraction symbol: -' 
print 'Trigonometric: math.sin(x),math.cos(x),math.tan(x)'
fun = raw_input('Y1 = ')

#Make blank list for the x and y coordinates
xlist = []
ylist = []
coordinates = ''

xval = 0
while xval < 4:
    xval = xval + 1
    xlist.append(float(xval))
    fun1 = fun.replace('x', '(' + str(xval) + ')')
    yval1 = eval(fun1)
    fun2 = fun.replace('x', '(' + str(xval+.000000001) + ')')
    yval2 = eval(fun2)
    yval = (yval2-yval1)/((xval+.000000001)-xval)
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
print 'FOR QUADRATICS: the equation of the derivative for', fun,'is y = ', m, 'x + ', yint
print 'Key for Graph:\nBlue - Original\nRed - Derivative'
#Establish what the coordinate plane looks like
def board():
    canvas.create_line(250, 0, 250, 500, fill="black", width=5)
    canvas.create_line(0, 250, 500, 250, fill="black", width=5)
    for i in range(1,20):
        x = 25*i
        canvas.create_line(0+x, 245, 0+x, 255, fill="black", width=3)
    for i in range(-10,10):
        y = 25*i
        canvas.create_line(245, 250+y, 255, 250+y, fill="black", width=3)


def graphcoor(xlist,ylist,counterx,fun):
    #graph the derivative
    xval = -10
    while xval < 10:
        xval = xval + .01
        fun1 = fun.replace('x', '(' + str(xval) + ')')
        yval1 = eval(fun1)
        fun2 = fun.replace('x', '(' + str(xval+.000000001) + ')')
        yval2 = eval(fun2)
        yval = (yval2-yval1)/((xval+.000000001)-xval)
        x1 = xval*25
        y1 = yval*25
        canvas.create_oval(250+x1, 250-y1, 250+x1, 250-y1, fill="red", outline = 'red', width =3)
    #Graph the original
    i = -10
    while i<10:
        x = i*25
        funct = fun.replace('x', '(' + str(i) + ')')
        fofi = eval(funct)
        y = fofi*25
        canvas.create_oval(250+x, 250-y, 250+x, 250-y, fill="blue", outline = 'blue', width =3)
        i = i + .01

if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    canvas.pack()
    board()
    graphcoor(xlist,ylist,counterx,fun)
    root.mainloop()
