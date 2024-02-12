import tkinter as tk

root = tk.Tk()
root.title("The Radiobutton Widget")
root.minsize(300,200)

for text, value in [("Apple", 1), ("Banana",2), ("Orange",3), ("Grape",4), ("Olive",5)]:
    tk.Radiobutton(root, text=text, value=value, indicatoron=0).pack()

root.mainloop()