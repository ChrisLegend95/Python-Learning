import tkinter as tk #Import tkinter GUI Toolkit


#---This is a function. It's created by using the line (def name_of_function():) this is so we can call it and the code is on standby, and listening to when it's called
def log_win():
    #--Global is use to allow diffrent bindings to travle out from the function and make othere functions learna dn work with the binding too.
    global username_vertify
    global password_vertify
    global username_entry1
    global password_entry1
    global screen2
    #--Toplevel widgets work as windows that are directly managed by the window manager. They do not necessarily have a parent widget on top of them.
    screen2 = tk.Toplevel()
    screen2.title("Login")
    screen2.geometry("300x250")
    #--Config for teh window is use mostly for background or other changes to teh main window/widget
    screen2.config()
    screen2.resizable(0, 0)
    
    #--Username_vertify is the binding and i sign it to tk.StringVar() for storage of the username and password that will be picked up and checked for after input is made.
    username_vertify = tk.StringVar()
    #---You can bind any word to "tk.StringVar()" to grab it after word from anothere function.
    password_vertify = tk.StringVar()

    tk.Label(screen2, text="Username").pack() #--Packing is a form organizes widgets in blocks before placing them in the parent widget.
    username_entry1 = tk.Entry(screen2, textvariable = username_vertify) #--This is a entry and it have (textvarable signed to username_vertify) this will grab what we put in and storage it for us to use later.
    username_entry1.pack()

    tk.Label(screen2, text="Password").pack()
    password_entry1 = tk.Entry(screen2, textvariable = password_vertify, show="*") #---In the end of this one you see (show="*") This is a reffrence to what the text will mask as so if you set (show="5") it will only show 5 and not Abcde123. Abcde123 is still ther is just hiden behind the numbmer 5
    password_entry1.pack()
    
    #--The relief style of a widget refers to certain simulated 3-D effects around the outside of the. you can use following "FLAT" "RAISED" "SUNKEN" "GROOVE" "RIDGE"
    tk.Button(screen2, text="Login", width=10, height=1, relief=tk.GROOVE, command=login_verify).pack(anchor="center")
    tk.Button(screen2, text="Exit", width=10, height=1, relief=tk.GROOVE, command=screen2.destroy).pack(anchor="center")
    #--The (command=function) is called for a function or a task, this is how we tell what happen when we press the button. as screen2.destroy will close the widget screen2 when pressed.


#--This function will verify if teh entry's are correct or not. here it's using if statment as you might have seen in Excel if you are familiar with it. It works the same way, on the basic way
def login_verify():
    
    #--This (screen3) don't need a mainloop when we have a mainloop for the root of the window already. this act like a child for the parent "screen" (can be found on teh bottom of the code)

    screen3 = tk.Tk()
    screen3.geometry("250x150")
    bt = tk.Button(screen3, text="Okej", command=screen3.destroy)
    bt.pack()
    #---See this window/widget as a temporary popup, for displaying some information or make a action.
    
    global login_verify
    username1 = username_vertify.get() #---With .get() we grabing what we storage in teh entryfield and using it as a binding for teh login_verify function.
    password1 = password_vertify.get()
    
    #---Here i set username and the password to get in, simple for one or more users to have.
    user = "Admin"
    password = "123"
    
    #--Here it check if the entry is empty or not, first check if it's empty if it's empty it will give a message. if not then it goes to next checkpoint.
    if username1 == "":
        if password1 == "":
            #---Screen3 is open as a widget to display a button and message with information. with tk.Lable(screen3) we get a new widget as we open it from a function and calling for the bases of the pass widget.
            tk.Label(screen3, text="you need to give \n username and password!", fg="red", width="300", height="2", font=("Calibri", 13)).pack()
            #---This else: check from the first if statment if the username have been given or not. if not it will display a message.
        else:
            tk.Label(screen3, text="You must give a username!", fg="red", width="300", height="2", font=("Calibri", 13)).pack()
    else:
        #---This else: is for when it passes the. it means there is something in the entryfield and it will check if it's correct.
        if username1 == user: #--Username1 is the entry we grab and we check if it's a 100% match with the user that is equal to username Admin
            if password1 == password: #---Here is the same thing as the username check, except it checking the password.
                tk.Label(screen3, text="Correct", fg="green", width="300", height="2", font=("Calibri", 15)).pack()
                #---This will display correct if it's all match teh credential.
            else:
                #--If password is wrong it will check and display a message with information.
                tk.Label(screen3, text="wrong password", fg="red", width="300", height="2", font=("Calibri", 15)).pack()
        else:
            #--Same as the one above except it's displaying the username is wrong.
            tk.Label(screen3, text="wrong username", fg="red", width="300", height="2", font=("Calibri", 15)).pack()

#This is the main window (screen) i use it as a function for easier work of code. insted of having the main window as a raw code i use function to make work easier around connection diffrent functions
def main_win():
    global screen
    screen = tk.Tk()
    screen.title("Welcome")
    screen.geometry("300x250")
    screen.resizable(0, 0)
    screen.config()
    #--Here is where it all start's. the button (login) is running (command=log_win) and will start the function of a window/widget to enter username and password.
    login = tk.Button(screen, text="Login", width="17", height="1", relief=tk.GROOVE, command=log_win)
    login.pack(padx=100, pady=100)
    #---The screen.mainloop() is importent to keep this widnow in loop. if it's closed everything will close and the login program will stop running.
    #--This window is the perent of all the windows created in this functions above, so it's working as a tree branch. If you cut down the tree, then everything will follow and fall.
    screen.mainloop()
#This main_win() is the first thing that runs of the code. This is calling the function for the main window as soon as you run the code. it's a way to say to the code. "Run this one when you start!"
#You can use this on diffrent functions as well as in after it preform a task it will open a window/widget or run a code in a function.
#We allways need something to activate the functions and diffrent lines of code. This is what we use buttons for, as a visual caller for a function. insdead of typing a commadn it's easier to have it all in one button and a function.
main_win()
