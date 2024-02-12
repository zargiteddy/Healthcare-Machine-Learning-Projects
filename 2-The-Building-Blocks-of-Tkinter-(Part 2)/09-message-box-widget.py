import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Messagebox Application")
root.minsize(300,200)

def show_info():
    messagebox.showinfo("Info", "learning is fun and practicing is clever.")

def show_warning():
    messagebox.showwarning("Notice", "Reminding you to practice today.")

def show_error():
    messagebox.showerror("Mistake", "Failing to practice is practicing to fail.")

def show_question():
    answer = messagebox.askquestion("Info", "Have you practiced today?")

    if answer == "yes":
        tk.Label(root, text="Good student").pack()
    else:
        tk.Label(root, text="Please practice").pack()

btninfo = tk.Button(root, text="Click Info", command = show_info).pack()
btnwarning = tk.Button(root, text="Click Warning", command = show_warning).pack()
btnerror = tk.Button(root, text="Click Error", command = show_error).pack()
btnquestion = tk.Button(root, text="Click Question", command = show_question).pack()

root.mainloop()