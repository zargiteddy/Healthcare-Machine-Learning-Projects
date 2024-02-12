import tkinter as tk

root = tk.Tk()
root.title("Multiple lines with Message")
root.minsize(300,200)

tk.Message(root, text=" Attack ships on fire off the shoulder of Orion. I watched C-beams glitter in the dark near the Tannhäuser Gate.",
         bg="lightblue", width=200, justify="center", relief="raised").pack()

root.mainloop()