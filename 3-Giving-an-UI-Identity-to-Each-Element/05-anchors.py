import tkinter as tk
from tkinter.font import Font

root = tk.Tk()
root.title("Widgets and Anchors")
root.minsize(300,200)

frame = tk.Frame(root).pack()
tk.Label(frame, text="North").pack(anchor="nw")


root.mainloop()