import tkinter as tk
from tkinter import messagebox
from database import insert_user

def register_user():
    username = entry_reg_username.get()
    password = entry_reg_password.get()
    
    if not username or not password:
        messagebox.showerror("Error", "All fields are required")
        return
    
    if insert_user(username, password):
        messagebox.showinfo("Success", "Registration successful")
        entry_reg_username.delete(0, tk.END)
        entry_reg_password.delete(0, tk.END)
        root.destroy()  # Close the registration window after success
    else:
        messagebox.showerror("Error", "Username already exists")

def show_register_page():
    global root, entry_reg_username, entry_reg_password
    root = tk.Tk()
    root.title("Register")
    root.geometry("300x200")

    tk.Label(root, text="New Username:").pack()
    entry_reg_username = tk.Entry(root)
    entry_reg_username.pack()

    tk.Label(root, text="New Password:").pack()
    entry_reg_password = tk.Entry(root, show="*")
    entry_reg_password.pack()

    tk.Button(root, text="Register", command=register_user).pack(pady=5)

    root.mainloop()
