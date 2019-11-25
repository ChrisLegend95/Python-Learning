import tkinter as tk


def log_win():
    global username_vertify
    global password_vertify
    global username_entry1
    global password_entry1
    global screen2
    screen2 = tk.Toplevel()
    screen2.title("Login")
    screen2.geometry("300x250")
    screen2.config()
    screen2.resizable(0, 0)

    username_vertify = tk.StringVar()
    password_vertify = tk.StringVar()

    tk.Label(screen2, text="Username").pack()
    username_entry1 = tk.Entry(screen2, textvariable = username_vertify)
    username_entry1.pack()

    tk.Label(screen2, text="Password").pack()
    password_entry1 = tk.Entry(screen2, textvariable = password_vertify, show="*")
    password_entry1.pack()

    tk.Button(screen2, text="Login", width=10, height=1, relief=tk.GROOVE, command=login_verify).pack(anchor="center")
    tk.Button(screen2, text="Exit", width=10, height=1, relief=tk.GROOVE, command=screen2.destroy).pack(anchor="center")



def login_verify():

    screen3 = tk.Tk()
    screen3.geometry("250x150")
    bt = tk.Button(screen3, text="Okej", command=screen3.destroy)
    bt.pack()
    
    global login_verify
    username1 = username_vertify.get()
    password1 = password_vertify.get()

    user = "Admin"
    password = "123"

    if username1 == "":
        if password1 == "":
            tk.Label(screen3, text="you need to give \n username and password!", fg="red", width="300", height="2", font=("Calibri", 13)).pack()
        else:
            tk.Label(screen3, text="You must give a username!", fg="red", width="300", height="2", font=("Calibri", 13)).pack()
    else:
        pass
        if username1 == user:
            if password1 == password:
                tk.Label(screen3, text="Correct", fg="green", width="300", height="2", font=("Calibri", 15)).pack()
            else:
                tk.Label(screen3, text="wrong password", fg="red", width="300", height="2", font=("Calibri", 15)).pack()
        else:
            tk.Label(screen3, text="wrong username", fg="red", width="300", height="2", font=("Calibri", 15)).pack()


def main_win():
    global screen
    screen = tk.Tk()
    screen.title("Welcome")
    screen.geometry("300x250")
    screen.resizable(0, 0)
    screen.config()

    login = tk.Button(screen, text="Login", width="17", height="1", relief=tk.GROOVE, command=log_win)
    login.pack(padx=100, pady=100)

    screen.mainloop()

main_win()