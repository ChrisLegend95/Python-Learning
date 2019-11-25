import tkinter as tk
from PIL import ImageTk,Image
import os
import io
from Login_sucess import tools

firstclick = True

#-------------[Switching to login window]-----------------------------
def next():
    screen.destroy()
    login()
#------------------------------------------------------------------------------------------
def passes():
    screen6.destroy()
    tools()
#----------------------[This will be called onnly for Birfday event]-----------------------------
def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if birfday_entry.get() == 'YYYY/MM/DD':
       birfday_entry.config(fg = "gray")
       birfday_entry.delete(0, "end") # delete all the text in the birfday_entry
       birfday_entry.insert(0, '') #Insert blank for user input
       birfday_entry.config(fg = 'black')
def on_focusout(event):
    if birfday_entry.get() == '':
        birfday_entry.insert(0, 'YYYY/MM/DD')
        birfday_entry.config(fg = 'grey')
#---------------------------------------------------------------------------------------------------------

#----------------------------[Main window for start]------------------------------------------------------

def main_win():
    global screen
    global im
    screen = tk.Tk()
    screen.title("Welcome")
    screen.geometry("300x250")
    screen.iconbitmap("Icon.ico")
    screen.resizable(0, 0)
    screen.config()

    ph = tk.PhotoImage(file="cmd.gif")
    im = tk.Label(screen, image=ph)
    im.pack(fill=tk.BOTH, expand=tk.TRUE)

    login = tk.Button(screen, text="Login", width="17", height="1", relief=tk.GROOVE, command=log_win)
    login.pack(side="right", in_=im, padx=10)

    registrate = tk.Button(screen, text="Register", width="17", height="1", relief=tk.GROOVE , command=reg_win)
    registrate.pack(anchor="center",side="left", in_=im, padx=10)

    screen.mainloop()

#-----------------------------[Login]---------------------------------
def log_win():
    global username_vertify
    global password_vertify
    global log_win
    global username_entry1
    global password_entry1
    global screen2
    screen2 = tk.Toplevel()
    screen2.title("Login")
    screen2.geometry("300x250")
    screen2.iconbitmap("Icon.ico")
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
#-----------------------------[Registration]------------------------------------
def reg_win():
    global screen1
    global reg_win
    global username
    global password
    global password_entry
    global username_entry
    global email
    global birfday
    global birfday_entry
    screen1 = tk.Toplevel(screen)
    screen1.title("Registrate")
    screen1.geometry("300x250")
    screen1.iconbitmap("Icon.ico")
    screen1.resizable(0, 0)

    username = tk.StringVar()
    password = tk.StringVar()
    email = tk.StringVar()
    birfday = tk.StringVar()

    lb2 = tk.Label(screen1, text="Username")
    lb2.pack(pady=10)
    username_entry = tk.Entry(screen1, textvariable = username)
    username_entry.pack()

    lb3 = tk.Label(screen1, text="Password")
    lb3.pack()
    password_entry = tk.Entry(screen1, textvariable = password)
    password_entry.pack()

    lb4 = tk.Label(screen1, text="Email")
    lb4.pack()
    email_entry = tk.Entry(screen1, textvariable = email, width="30")
    email_entry.pack()

    lb8 = tk.Label(screen1, text="Birfday")
    lb8.pack()

    birfday_entry = tk.Entry(screen1, textvariable = birfday)
    birfday_entry.insert(0, "YYYY/MM/DD")
    birfday_entry.config(fg = "gray")
    birfday_entry.bind("<FocusIn>", on_entry_click)
    birfday_entry.bind('<FocusOut>', on_focusout)
    birfday_entry.pack()

    tk.Button(screen1, text="Register", width="25", height="1", relief=tk.GROOVE, command=user_check).pack(side="bottom")
    tk.Button(screen1, text="Exit", width="25", height="1", relief=tk.GROOVE, command=screen1.destroy).pack(side="bottom")
#-------------[Register check]-------------------------------------------------------------------
def user_check():
    global user_check
    username_vertify = tk.StringVar()
    user_check = username_vertify.get()

    username_info = username.get()

    dir = os.path.join("C:\\Users\\LegitLegend\\Documents\\Project\\Project\\Accounts\\"+username_info)
    if not os.path.exists(dir):
        register_user()
    else:
        fail()
        screen3.iconbitmap("Icon.ico")
        tk.Label(screen3, text="Username already exists", fg="red", bg="light blue", width="300", height="2", font=("Calibri", 15)).pack()

#--------------------------[user allready made window]-------------------------------------------
def fail():
    global screen3
    screen3 = tk.Tk()
    screen3.geometry("250x125")
    screen3.resizable(0, 0)

    tk.Button(screen3, text="OK", width="25", height="1", relief=tk.GROOVE, command=screen3.destroy).pack(side="bottom")

#--------------------------[Login window/ can be what ever you want]---------------------------------------

#----------------------------[Registration script]-----------------------------------------------
def register_user():
    global register_user
    global username_info
    global password_info
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    year_info = birfday.get()

    dir = os.path.join("C:\\Users\\LegitLegend\\Documents\\Project\\Project\\Accounts\\"+username_info)
    if not os.path.exists(dir):
        os.mkdir(dir)


    file=open("C:\\Users\\LegitLegend\\Documents\\Project\\Project\\Accounts\\"+username_info+"\\username.txt", "w+")
    file.write(username_info)
    file=open("C:\\Users\\LegitLegend\\Documents\\Project\\Project\\Accounts\\"+username_info+"\\password.txt", "w+")
    file.write(password_info)
    file=open("C:\\Users\\LegitLegend\\Documents\\Project\\Project\\Accounts\\"+username_info+"\\info.txt", "w+")
    file.write("Email adress:" "\n" +email_info +"\n" "\n" "Birfday:" "\n"+ year_info + "\n")
    print("fodler created")
    file.close()
    sucess()

    # screen4.iconbitmap("Icon.ico")
    tk.Label(screen4, text="Registration Sucess", fg="green", bg="light blue", width="300", height="2", font=("Calibri", 18)).pack()
#--------------------------[Sucess registration]-------------------------------------------------------
def sucess():
    global screen4
    screen4 = tk.Tk()
    screen4.title("")
    screen4.geometry("300x225")
    screen4.resizable(0, 0)
    screen4.iconbitmap("Icon.ico")

    bt_exit = tk.Button(screen4, text="OK", width="25", height="1", relief=tk.GROOVE, command=done)
    bt_exit.pack()
#-----------[When registrate is done]-----------------------------
def done():
    screen4.destroy()
    screen1.destroy()

#------------------------------[Login script]-----------------------------------------------------------
def login_verify():
    
    global login_verify
    username1 = username_vertify.get()
    password1 = password_vertify.get()

    dir = os.path.join("C:\\Users\\LegitLegend\\Documents\\Project\\Project\\Accounts\\"+username1)
    if not os.path.exists(dir):
        fail()
        
        screen3.title("ERROR")
        screen3.iconbitmap("Icon.ico")
        tk.Label(screen3, text="This user is not in the system", fg="red", bg="light blue", width="300", height="2", font=("Calibri", 15)).pack()
    

    with open("C:\\Users\\LegitLegend\\Documents\\Project\\Project\\Accounts\\"+username1+"\\username.txt") as f:
        check = f.readline()
    
    name = check.rstrip()
    print("reading username compleated")


    with open("C:\\Users\\LegitLegend\\Documents\\Project\\Project\\Accounts\\"+username1+"\\password.txt") as f:
        check = f.readline()

    paword = check.rstrip()
    print("reading password compleated")

    if username1 == name:
        if password1 == paword:
            next()
        else:
            print("wrong password")
    else:
        fail()
        
        tk.Label(screen3, text="user is not in the system", fg="red", bg="light blue", width="300", height="2", font=("Calibri", 15)).pack()

#------------------------[Program window start]-----------------------------------
global login
global tools
def login():
    global screen6
    screen6 = tk.Tk()
    screen6.geometry("350x200")
    screen6.title("Welcome")
    screen6.iconbitmap("Icon.ico")
    screen6.resizable(0, 0)

    tk.Label(screen6, text="Login Sucessful", fg="green", width="300", height="2", font=("Calibri", 18)).pack()

    bt = tk.Button(screen6, text="Open tools", command=passes)
    bt.pack()
    

    screen6.mainloop()


main_win()
