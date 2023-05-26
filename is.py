import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class SignInApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x150")
        self.root.resizable(False, False)
        self.root.title("Sign In")

        self.email = tk.StringVar()
        self.password = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.signin = ttk.Frame(self.root)
        self.signin.pack(padx=10, pady=10, fill="x", expand=True)

        email_label = ttk.Label(self.signin, text="Email Address:")
        email_label.pack(fill="x", expand=True)

        email_entry = ttk.Entry(self.signin, textvariable=self.email)
        email_entry.configure(height=2)  # Set the height to 2 lines
        email_entry.pack(fill="x", expand=True)
        email_entry.focus()

        password_label = ttk.Label(self.signin, text="Password:")
        password_label.pack(fill="x", expand=True)

        password_entry = ttk.Entry(self.signin, textvariable=self.password, show="*")
        password_entry.configure(height=2)  # Set the height to 2 lines
        password_entry.pack(fill="x", expand=True)

        login_button = ttk.Button(self.signin, text="Login", command=self.login_clicked)
        login_button.pack(fill="x", expand=True, pady=10)

    def login_clicked(self):
        msg = (
            f"You entered email: {self.email.get()} and password: {self.password.get()}"
        )
        showinfo(title="Information", message=msg)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SignInApp()
    app.run()
