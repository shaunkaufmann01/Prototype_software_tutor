from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
root.geometry("%dx%d+%d+%d" % (100, 40, 100, 100))

root.mainloop()
