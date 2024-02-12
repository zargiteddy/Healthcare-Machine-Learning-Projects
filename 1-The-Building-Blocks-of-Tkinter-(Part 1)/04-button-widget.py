import tkinter as tk

root = tk.Tk()
root.title("The Button Widget")

btn = tk.Button(root, text="Click Me!",relief="raised").pack()
btn = tk.Button(root, text="Click Me!",relief="sunken").pack()
btn = tk.Button(root, text="Click Me!",relief="flat").pack()
btn = tk.Button(root, text="Click Me!",relief="ridge").pack()
btn = tk.Button(root, text="Click Me!",relief="groove").pack()
btn = tk.Button(root, text="Click Me!",relief="solid").pack()

root.mainloop()