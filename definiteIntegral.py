#Zev
#2/26/16

from Tkinter import *

#Zev Stravitz
#9/27/15
#This time with graph of original
import math
from Tkinter import *

print 'Welcome to the derivative calculator/grapher for all functions'
print 'Type in your function as thus: \nMultiplication symbol: *\n Exponent symbol: **\n Addition symbol: +\n Subtraction symbol: -' 
print 'Trigonometric: math.sin(x),math.cos(x),math.tan(x)'
fun = raw_input('Y1 = ')

#Make blank list for the x and y coordinates
coordinates = ''

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

def graphcoor(fun):
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
    graphcoor(fun)
    root.mainloop()
