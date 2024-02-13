import tkinter as tk
import random

root = tk.Tk()
root.title("placing widget")
root.minsize(300,200)

btn = tk.Button(root, text="My Place")

btn.place(x=20, y=20, height=60, width=80)

root.mainloop()