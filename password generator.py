import tkinter as tk
import random
import string

def generate_password():
    chars = ""

    if lower_var.get():
        chars += string.ascii_lowercase
    if upper_var.get():
        chars += string.ascii_uppercase
    if digits_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        password_var.set("Select at least one option")
        return

    password = "".join(
        random.choice(chars)
        for _ in range(length_var.get())
    )

    password_var.set(password)

def copy_password():
    if password_var.get():
        root.clipboard_clear()
        root.clipboard_append(password_var.get())

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

password_var = tk.StringVar()
length_var = tk.IntVar(value=12)

lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Label(root,text="Password Generator",font=("Arial", 16, "bold")).pack(pady=10)
tk.Entry(root, textvariable=password_var,font=("Arial", 14),justify="center",width=30).pack(pady=10)
tk.Label(root, text="Password Length").pack()
tk.Scale(root,from_=8,to=24,orient="horizontal",variable=length_var).pack()

tk.Checkbutton(root, text="Lowercase", variable=lower_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Uppercase", variable=upper_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Numbers", variable=digits_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Symbols", variable=symbols_var).pack(anchor="w", padx=50)

tk.Button(root,text="Generate Password",width=20,command=generate_password).pack(pady=10)
tk.Button(root,text="Copy Password",width=20,command=copy_password).pack()

root.mainloop()