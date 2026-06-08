import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for r, row in enumerate(buttons, start=1):
    for c, text in enumerate(row):
        if text == '=':
            btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
        else:
            btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t))
        btn.grid(row=r, column=c, padx=5, pady=5)

tk.Button(root, text="C", width=22, height=2,
          command=clear).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()