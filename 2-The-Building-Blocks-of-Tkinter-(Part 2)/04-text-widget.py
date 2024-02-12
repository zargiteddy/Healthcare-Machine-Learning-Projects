import tkinter as tk
from PIL import Image, ImageTk

image = Image.open("food2.jpg")
image = image.resize((500,345))

root = tk.Tk()
root.title("The Text Widget")
root.minsize(300,200)

img = ImageTk.PhotoImage(image)

text = tk.Text(root)
text.insert("insert", "The First Line in the text widget...\n")
text.insert("insert", "The Second Line in the text widget...")
text.image_create("end", image=img)

text.pack()

text.tag_add("here","1.0","1.36")
text.tag_add("next","2.0","2.36")
text.tag_config("here",background="orange",font="times")
text.tag_config("next",background="yellow",font="calibri")

root.mainloop()