import tkinter as tk
import random

root = tk.Tk()
root.title("Columns and Rows with Grid")
root.minsize(300,200)

for r in range(10):
    for c in range(10):
        tk.Button(root,text="R%s--C%s"%(r,c), bg="yellow").grid(row=r, column=c, padx=3, pady=2)

root.mainloop()