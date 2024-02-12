import tkinter as tk

root = tk.Tk()
root.title("Widgets in window with frame widget")
root.minsize(300,200)

frame = tk.Frame(root, bg="pink", height=400, width=400)

label = tk.Label(frame, text = " And blood-black nothingness began to spin. And dreadfully distinct against the dark, a tall white fountain played.", 
                 bg="lightgreen", font="calibri", wraplength=300).pack()

for text, value in [("Apple", 1), ("Banana",2), ("Orange",3), ("Grape",4), ("Olive",5)]:
    tk.Radiobutton(frame, text=text, value=value, indicatoron=0, width=20).pack()

frame.pack()

root.mainloop()