import tkinter as tk

def on_click(event):
    current_text = entry.get()
    clicked_text = event.widget.cget("text")
    if clicked_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif clicked_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, clicked_text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack(fill=tk.BOTH, expand=True)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("(", ")", "=", "")
]

for row in buttons:
    row_frame = tk.Frame(buttons_frame)
    row_frame.pack()
    for button_text in row:
        button = tk.Button(row_frame, text=button_text, font=("Arial", 20), padx=20, pady=10)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        button.bind("<Button-1>", on_click)

root.mainloop()
