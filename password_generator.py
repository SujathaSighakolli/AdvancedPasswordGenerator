import tkinter as tk
from tkinter import ttk, messagebox
import string
import random

# Main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x420")
root.config(bg="#1e1e2f")

# Global variables
password_var = tk.StringVar()
password_length = tk.IntVar(value=12)

# Title
title = tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 18, "bold"), bg="#1e1e2f", fg="#f9f9f9")
title.pack(pady=10)

# Options Frame
frame = tk.Frame(root, bg="#2a2a3d")
frame.pack(padx=20, pady=10, fill="x")

# Character Options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=False)
exclude_similar_var = tk.BooleanVar(value=False)

# Length
tk.Label(frame, text="Password Length:", bg="#2a2a3d", fg="white", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5)
tk.Spinbox(frame, from_=4, to=64, textvariable=password_length, width=5).grid(row=0, column=1, sticky="w", padx=5)

# Checkboxes
tk.Checkbutton(frame, text="Include Uppercase", variable=upper_var, bg="#2a2a3d", fg="white", selectcolor="#2a2a3d", activebackground="#2a2a3d").grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Lowercase", variable=lower_var, bg="#2a2a3d", fg="white", selectcolor="#2a2a3d", activebackground="#2a2a3d").grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Digits", variable=digit_var, bg="#2a2a3d", fg="white", selectcolor="#2a2a3d", activebackground="#2a2a3d").grid(row=3, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Symbols", variable=symbol_var, bg="#2a2a3d", fg="white", selectcolor="#2a2a3d", activebackground="#2a2a3d").grid(row=4, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Exclude Similar Characters (1, l, I, 0, O)", variable=exclude_similar_var, bg="#2a2a3d", fg="white", wraplength=400, justify="left", selectcolor="#2a2a3d", activebackground="#2a2a3d").grid(row=5, column=0, columnspan=2, sticky="w")

# Password Entry
tk.Entry(root, textvariable=password_var, font=("Courier", 14), width=30, justify="center").pack(pady=10)

# Generate Password
def generate_password():
    chars = ""
    if upper_var.get(): chars += string.ascii_uppercase
    if lower_var.get(): chars += string.ascii_lowercase
    if digit_var.get(): chars += string.digits
    if symbol_var.get(): chars += string.punctuation

    if exclude_similar_var.get():
        for c in "Il1O0":
            chars = chars.replace(c, '')

    if not chars:
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return

    length = password_length.get()
    pw = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(pw)

# Copy to clipboard
def copy_to_clipboard():
    pw = password_var.get()
    if pw:
        root.clipboard_clear()
        root.clipboard_append(pw)
        root.update()
        messagebox.showinfo("Copied", "✅ Password copied to clipboard!")
    else:
        messagebox.showwarning("Oops!", "No password to copy!")

# Strength checker
def check_strength():
    pw = password_var.get()
    score = 0
    if len(pw) >= 12: score += 1
    if any(c.islower() for c in pw): score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in string.punctuation for c in pw): score += 1

    if score >= 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Moderate 🛡️"
    else:
        strength = "Weak ⚠️"

    messagebox.showinfo("Password Strength", f"Password Strength: {strength}")

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="🔁 Generate", command=generate_password, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=12).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="📋 Copy", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Helvetica", 12), width=12).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="🔎 Check Strength", command=check_strength, bg="#FF9800", fg="white", font=("Helvetica", 12), width=28).grid(row=1, column=0, columnspan=2, pady=10)

# Run the App
root.mainloop()
