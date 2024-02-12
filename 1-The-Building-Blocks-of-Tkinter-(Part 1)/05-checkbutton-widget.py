import tkinter as tk

root = tk.Tk()
root.title("The Checkbutton Widget")
root.minsize(300,200)

tk.Label(root, text="Select Your Favorite Fruits")
tk.Checkbutton(root, text="Strawberry").pack()
tk.Checkbutton(root, text="Guava").pack()
tk.Checkbutton(root, text="Mango").pack()
tk.Checkbutton(root, text="Orange").pack()
tk.Checkbutton(root, text="Aple").pack()
tk.Checkbutton(root, text="Zargitedy", state="disabled").pack()

root.mainloop()