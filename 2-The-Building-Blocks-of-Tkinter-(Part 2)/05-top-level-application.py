import tkinter as tk

root = tk.Tk()
root.title("TopLevel Application")
root.minsize(300,200)

toplevel = None

def  top():
    global toplevel
    toplevel = tk.Toplevel(root)
    label = tk.Label(toplevel, text="Baseline Test").pack()
    terms = tk.Message(toplevel, text="When you're not performing your duties, do they keep you in a little box? Interlinked.",
                     width=300).pack()
    radio = tk.Radiobutton(toplevel, text="Interlinked", command=agree, state="normal", value=1).pack()
    radio = tk.Radiobutton(toplevel, text="Silent", command=root.quit, state="normal").pack()

def agree():
    global toplevel
    tk.Label(root, text=" We're done. You can pick up your bonus").pack()
    toplevel.destroy

btn = tk.Button(root, text="Recite your baseline", command=top).pack()

root.mainloop()