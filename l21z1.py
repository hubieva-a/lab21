import tkinter
from tkinter import *

def draw_oval(event):
    if variable1.get() == 1:
        x1 = textbox_x1.get()
        y1 = textbox_y1.get()
        x2 = textbox_x2.get()
        y2 = textbox_y2.get()
        new_canvas.create_oval(x1, y1, x2, y2, width=2, fill='grey')

def draw_rectangle(event):
    if variable1.get() == 0:
        x1 = textbox_x1.get()
        y1 = textbox_y1.get()
        x2 = textbox_x2.get()
        y2 = textbox_y2.get()
        new_canvas.create_rectangle(x1, y1, x2, y2, fill='grey')

def new_window(event):
    sub = tkinter.Toplevel()
    textbox_x1 = Text(sub, width=5, height=1)
    textbox_y1 = Text(sub, width=5, height=1)
    textbox_x2 = Text(sub, width=5, height=1)
    textbox_y2 = Text(sub, width=5, height=1)
    variable1 = IntVar()
    variable1.set(0)
    radiobutton1 = Radiobutton(sub, text='Прямоугольник',
                               variable=variable1, value=0)
    radiobutton2 = Radiobutton(sub, text='Овал',
                               variable=variable1, value=1)
    but1 = Button(sub, text='Нарисовать', width=20)
    label1 = Label(sub, text='x1', width=5)
    label2 = Label(sub, text='y1', width=5)
    label3 = Label(sub, text='x2', width=5)
    label4 = Label(sub, text='y2', width=5)

    radiobutton1.bind('<Button-1>', draw_oval)
    radiobutton2.bind('<Button-1>', draw_rectangle)

    label1.pack(side=LEFT)
    textbox_x1.pack(side=LEFT)
    label2.pack(side=LEFT)
    textbox_y1.pack(side=LEFT)
    label3.pack(side=LEFT)
    textbox_x2.pack(side=LEFT)
    label4.pack(side=LEFT)
    textbox_y2.pack(side=LEFT)
    radiobutton1.pack(side=BOTTOM)
    radiobutton2.pack(side=BOTTOM)
    but1.pack(side=BOTTOM)

root = Tk()

new_canvas = Canvas(root, width=200, height=200, bg='white')
but2 = Button(text='Добавить фигуру')

but2.bind('<Button-1>', new_window)

new_canvas.pack()
but2.pack()

root.mainloop()