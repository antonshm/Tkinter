from tkinter import *
from random import randrange as rnd, choice
colors =['#ff0000','#000000']
x = 0 #coordinate
y = 0 #coordinate
r = 0 #radius
points = 0
miss = 0
def new_ball():
    global x, y, r, res
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    res = canv.create_text(60, 20, text=str(points) + '/' + str(miss),   	font='Arial 20')
    canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), 	width=0)
    root.after(1000, new_ball)
    pass
def click(event):
      global points, miss, res
      if abs(x - event.x) < r and abs(y - event.y) < r: #clicked the ball
        points += 1
        canv.delete(ALL)
        res = canv.create_text(60, 20, text=str(points) + '/' + str(miss),   	font='Arial 20')
      else: #did not click on the ball
        miss += 1
        canv.delete(ALL)
        res = canv.create_text(60, 20, text=str(points) + '/' + str(miss), 	font='Arial 20')
      pass
root=Tk()
root.geometry('800x550')
root.title('Eliminate all terorists')
canv = Canvas(root, width=800,height=550, bg='lightgreen')
canv.pack()

root.config(cursor='cross_reverse')
root.after(1000,new_ball)
canv.bind('<Button-1>',click)
root.mainloop()
