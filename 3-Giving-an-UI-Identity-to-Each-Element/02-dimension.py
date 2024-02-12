import tkinter as tk

root = tk.Tk()
root.title("Dimension Measurement")
root.minsize(300,200)

tk.Message(root, text="Ipsum deserunt dolore excepteur sint ullamco culpa irure. Nisi aliquip nulla anim anim consectetur anim cillum duis do pariatur. Quis sunt ex pariatur dolor est eu aute non et voluptate ut sit reprehenderit voluptate. Ipsum dolor non labore elit.",
width="20m").pack()

tk.Message(root, text="Ipsum deserunt dolore excepteur sint ullamco culpa irure. Nisi aliquip nulla anim anim consectetur anim cillum duis do pariatur. Quis sunt ex pariatur dolor est eu aute non et voluptate ut sit reprehenderit voluptate. Ipsum dolor non labore elit.",
width="20p").pack()

root.mainloop()