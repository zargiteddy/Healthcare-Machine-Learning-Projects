import tkinter as tk

root = tk.Tk()
root.title("Colors")
root.minsize(300,200)

tk.Button(root, text="Colors", background="red").pack() 
tk.Button(root, text="Colors", foreground="red").pack() 
tk.Button(root, text="Colors", activebackground="red").pack() 
tk.Button(root, text="Colors", activeforeground="red").pack() 
tk.Button(root, text="Colors", disabledforeground="red", state="disabled").pack() 

root.mainloop()