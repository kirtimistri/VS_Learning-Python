import tkinter as tk
from tkinter import messagebox
from database import verify_user
from registration import show_register_page


def login_user():
    username = entry_login_username.get()
    password = entry_login_password.get()
    
    if verify_user(username, password):
        messagebox.showinfo("Success", "Login successful")
        entry_login_username.delete(0, tk.END)
        entry_login_password.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Invalid username or password")


root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

tk.Label(root, text="Username:").pack()
entry_login_username = tk.Entry(root)
entry_login_username.pack()

tk.Label(root, text="Password:").pack()
entry_login_password = tk.Entry(root, show="*")
entry_login_password.pack()

tk.Button(root, text="Login", command=login_user).pack(pady=5)
tk.Button(root, text="Register", command=show_register_page).pack()

root.mainloop()
