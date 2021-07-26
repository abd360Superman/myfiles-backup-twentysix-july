from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox as mb

tk = Tk()
tk.geometry('250x80')
tk.title('Create a file!')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
tk.update()

filename = ''
filetype = ''
filepath = ''

filename_label = Label(tk, text='Filename', font=('calibre', 10, 'bold'))
filename_entry = Entry(tk, font=('calibre', 10, 'normal'))
filename_label.grid(row=0, column=0)
filename_entry.grid(row=0, column=1)

filetype_label = Label(tk, text='Filetype', font=('calibre', 10, 'bold'))
filetype_entry = Entry(tk, font=('calibre', 10, 'normal'))
filetype_label.grid(row=1, column=0)
filetype_entry.grid(row=1, column=1)

def select_create():
    filename = filename_entry.get()
    filetype = filetype_entry.get()
    
    filepath = filedialog.askdirectory()
    path = os.path.join(filepath, filename+'.'+filetype)
        
    with open(path, 'w') as fp:
        pass
    
    mb.showinfo('confirmation', 'File Created!')
    os.startfile(path)

directory = Button(text='Select Location', bg='Skyblue', command=select_create)
directory.grid(row=5, column=0)
