from tkinter import *
import random

def click_smiley_face(event):
    random_x = random.randint(0, 400)
    random_y = random.randint(0, 400)
    label1.place(x=random_x, y=random_y)

root = Tk()

root.geometry("400x400")
img = PhotoImage(file='smiley_face.png')
but1 = Button(image=img, height=30, width=30)
label1 = Label(height=30, width=30, image=img)

but1.bind('<Button-1>', click_smiley_face)
but1.pack(side=BOTTOM)
root.mainloop()