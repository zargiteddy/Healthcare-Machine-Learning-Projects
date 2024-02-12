import tkinter as tk
from tkinter.font import Font

root = tk.Tk()
root.title("Change text appearance with fonts")
root.minsize(300,200)

font1 = Font(
    family="helvetica",
    size=18,
    weight="bold",
    slant="italic",
    underline=1,
    overstrike=1
)

font2 = Font(
    family="courier",
    size=14,
    weight="bold",
    slant="roman",
    underline=1,
    overstrike=0
)

tk.Label(root, text="hello tkinter", font=font1).pack()
tk.Label(root, text="hello tkinter", font=font2).pack()

root.mainloop()