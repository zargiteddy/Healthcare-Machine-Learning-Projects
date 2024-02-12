import tkinter as tk

root = tk.Tk()
root.title("Label")

label = tk.Label(root, text = " My unmatched perspicacity coupled with my sheer indefatigability makes me a feared opponent in any realm of human endeavor.", 
                 bg="lightgreen", font="calibri", wraplength=500, padx=20, pady=20)

label.pack()
root.mainloop()