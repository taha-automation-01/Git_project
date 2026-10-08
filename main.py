# main.py
import tkinter as tk
from tkinter import messagebox

def show_greeting():
    name = entry.get()
    if name.strip():
        messagebox.showinfo("Greeting", f"Hello, {name}!\nWelcome to Git and GitHub GUI.")
    else:
        messagebox.showwarning("Warning", "Please enter your name!")

def clear_input():
    entry.delete(0, tk.END)

# Setup UI
root = tk.Tk()
root.title("Git Greeting App")
root.geometry("300x180")

label = tk.Label(root, text="Enter your name:")
label.pack(pady=5)

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

btn_greet = tk.Button(root, text="Greet Me", command=show_greeting)
btn_greet.pack(pady=5)

# قابلیت جدید: دکمه پاک کردن
btn_clear = tk.Button(root, text="Clear", command=clear_input)
btn_clear.pack(pady=5)

root.mainloop()
