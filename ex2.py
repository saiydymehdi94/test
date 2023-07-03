import tkinter as tk

def button_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click me", command=button_click)
button.pack()

root.mainloop()

