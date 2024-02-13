import tkinter as tk
import random

root = tk.Tk()
root.title("The Packer")
root.minsize(300,200)

tk.Button(root, text="default position").pack()
tk.Button(root, text="default position attributes").pack(side="bottom",anchor="center",
                                                         fill="x",expand=1)
root.mainloop()