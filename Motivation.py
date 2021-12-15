import tkinter as tk
import tkinter.ttk as ttk
import random


def welcome():
    global root
    root = tk.Tk()
    root.geometry("350x160")
    root.resizable(0, 0)
    root.title("Welcome")

    tx = tk.ttk.Label(root, text="Are you ready for some motivation?")
    tx.place(y=20, x=80)

    bt = tk.ttk.Button(root, text="YES!", command=name)
    bt.place(y=80, x=60)

    bt2 = tk.ttk.Button(root, text="NO :(", command=exit)
    bt2.place(y=80, x=200)

    root.mainloop()


def name():
    root.destroy()

    global here

    root2 = tk.Tk()
    root2.geometry("350x160")
    root2.resizable(0, 0)
    root2.title("Whats your name?")

    here = tk.StringVar()

    tx = tk.ttk.Label(root2, text="So what is your name? \nPlz tell me \ni want to know :)")
    tx.place(y=20, x=110)
    
    tx2 = tk.ttk.Label(root2, text="name:")
    tx2.place(y=80, x=70)

    here = tk.ttk.Entry(root2)
    here.place(y=80, x=110)
    
    bt = tk.ttk.Button(root2, text="Give me motivation!", command=script)
    bt.place(y=130, x=150)

    bt2 = tk.ttk.Button(root2, text="Exit", command=exit)
    bt2.place(y=130, x=270) 

    root2.mainloop()


def script():

    global screen3

    screen3 = tk.Tk()
    screen3.geometry("350x160")
    screen3.resizable(0, 0)
    screen3.title("Motivation!")

    bt = tk.ttk.Button(screen3, text="Okej", command=screen3.destroy)
    bt.place(anchor=tk.CENTER, y=100, x=170)
    
    global username1
    username1 = here.get()

    if username1 == "":
        tk.Label(screen3, text="You must give a name :(", width="300", height="2").place(anchor=tk.CENTER, y=50, x=170)
    else:
        pass
        if username1 == username1:
            if username1 == "bob":
                tk.Label(screen3, text="Sorry no bob allowed motivation :(", width="300", height="2").place(anchor=tk.CENTER, y=50, x=170)
            else:
                motivation()

def motivation():
    screen3.destroy()

    root3 = tk.Tk()
    root3.geometry("350x160")
    root3.resizable(0, 0)
    root3.title("Feel the motivation!")
    

    first = ("wow, you do look amazing today " + username1 + " :O", 
    "I know you can do it " + username1 + "!" + " :)",
    "You are truly a good looking person " + username1 + " ;)",
    "" + username1 + " you are the best! B)",
    "" + username1 + " the day is yours, enjoy it! :D",
    "" + username1 + " you can do anything, I know you can :)",
    "The world is in your hand " + username1,
    "have I told you I love you? " + username1 + "   ... no? Well i do :)",
    )
    second2 = ("Coder", "Hot", "Spider,", "Poop", "NO!", "Pasta", "Cat", "Sofa", "Genital", "Wait!", "Out", "Hello?", "Hitler", "Tank", "Delete", "But", "Fuck", "Vegan", "Man", "Hacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Killer", "Woman", "Programmer", "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper", "Quickscoper", "Sniper", "Hero", "miscarriage", "Nincompoop", "Fatuous")
    second = ("Coder", "Hot", "Spider,", "Poop", "NO!", "Pasta", "Cat", "Sofa", "Genital", "Wait!", "Out", "Hello?", "Hitler", "Tank", "Delete", "But", "Fuck", "Vegan", "Man", "Hacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Killer", "Woman", "Programmer", "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper", "Quickscoper", "Sniper", "Hero", "miscarriage", "Nincompoop", "Fatuous")
    firrst = random.choice(first)
    seccond = random.choice(second)
    seccond2 = random.choice(second2)
    name = (firrst)

    word = ("[ " + seccond + " " + seccond2 + " ]")

    text = tk.Label(root3, text=name)
    text.place(anchor=tk.CENTER, y=25, x=170)

    text = tk.Label(root3, text="[word of the day]")
    text.place(anchor=tk.CENTER, y=70, x=170)

    text = tk.Label(root3, text=word)
    text.place(anchor=tk.CENTER, y=100, x=170)

welcome()
