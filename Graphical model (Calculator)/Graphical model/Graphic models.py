import tkinter as tk

def show_text():
    text = entry.get()
    label.config(text=text)

root = tk.Tk()
root.title("Entry Widget")
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Show Text", command=show_text)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
