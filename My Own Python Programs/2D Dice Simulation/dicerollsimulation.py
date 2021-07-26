from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas(tk, width=100, height=150, highlightthickness=0)
canvas.pack()
tk.update()

image = [PhotoImage(file='1dice.gif'),
         PhotoImage(file='2dice.gif'),
         PhotoImage(file='3dice.gif'),
         PhotoImage(file='4dice.gif'),
         PhotoImage(file='5dice.gif'),
         PhotoImage(file='6dice.gif')]

def dice_roll():
    random_picture = random.choice(image)
    pic = canvas.create_image(0, 0, anchor=NW, image=random_picture)
    time.sleep(0.1)
    for i in range(1, 50):
        random_picture = random.choice(image)
        canvas.itemconfig(pic, image=random_picture)
        time.sleep(0.1)

btn = Button(text='Roll the Dice!', bg='skyblue', command=dice_roll)
btn.pack()
