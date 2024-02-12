import tkinter as tk

root = tk.Tk()
root.title("My Tkinter App")
root.minsize(300,200)

# activebackground is a label attribute
tk.Label(root, activebackground="lightblue")

root.mainloop()