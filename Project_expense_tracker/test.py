import tkinter as tk
from tkinter.constants import INSERT
frm = tk.Frame()
entr = tk.Entry(foreground='black', background='white', width=40)
entr.pack()
entr.insert(0, "Mazfaka!")
tk.mainloop()
