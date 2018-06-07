#Zev Stravitz
#11/6/16
#3D grapher



import math
from Tkinter import *

print 'Welcome to the 3D point grapher'
x_comp = int(raw_input('X component: '))
y_comp = int(raw_input('Y component: '))
z_comp = int(raw_input('Z component: '))


def graphAxis():
    canvas.create_line(250, 0, 250, 250, fill="red", width=5)
    canvas.create_line(250, 250, 74, 426, fill="red", width=5)
    canvas.create_line(250, 250, 500, 250, fill="red", width=5)

    for i in range(1,10):
        x = 25*i
        canvas.create_line(250+x,245, 250+x,255, fill="blue", width=3)
    for i in range(1,10):
        y = 25*i
        canvas.create_line(245, y, 255, y, fill="blue", width=3)
    for i in range(1,10):
        x = 25*i*.7
        y = 25*i*.7
        canvas.create_line(250-x-5, 250 + y, 250-x+5, 250 + y, fill="blue", width=3)


def graphCoor():
    #Graph the y component
    final_y = 250 + y_comp*25
    canvas.create_line(250,250,final_y,250, fill="green", width=3)

    #Graph the Z component
    final_z = 250 - z_comp*25
    canvas.create_line(final_y,250,final_y,final_z, fill="green", width=3)

    #Finish rectangle
    canvas.create_line(250,final_z,final_y,final_z, fill="green", width=3)
    canvas.create_line(250,250,250,final_z, fill="green", width=3)

    #Make the rectangle
    canvas.create_line(final_y,final_z,(final_y+x_comp*25*.707),(final_z-x_comp*25*.707), fill="green", width=3) #important one
    canvas.create_line(250,final_z,(250+x_comp*25*.707),(final_z-x_comp*25*.707), fill="green", width=3)
    canvas.create_line(final_y,250,(final_y+x_comp*25*.707),(250-x_comp*25*.707), fill="green", width=3)
    canvas.create_line(250,250,(250+x_comp*25*.707),(250-x_comp*25*.707), fill="green", width=3)
    
    canvas.create_line((250+x_comp*25*.707),(250-x_comp*25*.707),(250+x_comp*25*.707),(final_z-x_comp*25*.707), fill="green", width=3)
    canvas.create_line((final_y+x_comp*25*.707),(250-x_comp*25*.707),(final_y+x_comp*25*.707),(final_z-x_comp*25*.707), fill="green", width=3)
    canvas.create_line((250+x_comp*25*.707),(250-x_comp*25*.707),(final_y+x_comp*25*.707),(250-x_comp*25*.707), fill="green", width=3)
    canvas.create_line((250+x_comp*25*.707),(final_z-x_comp*25*.707),(final_y+x_comp*25*.707),(final_z-x_comp*25*.707), fill="green", width=3)

    

    #Draw the vector
    canvas.create_line(250,250,(final_y+x_comp*25*.707),(final_z-x_comp*25*.707), fill="black", width=4)

    
if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    canvas.pack()
    graphAxis()
    graphCoor()
    root.mainloop()
