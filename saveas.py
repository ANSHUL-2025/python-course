from tkinter import *

from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry('300x300')

def save():
    files = [
        ('All Files', '*.*'),
        ('Python Files', '*.py'),
        ('Text Document', '*.txt')
    ]
    file = asksaveasfile(filetypes=files, defaultextension=files)

btn = Button(root, text='Save', command=save)
btn.pack(side=TOP, pady=20)

root.mainloop()