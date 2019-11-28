import random
import tkinter as tk

def name_generator_Eng():
    global nameout
    nameout.delete(1.0,"end")
    first = ("Super", "Retarded", "Shit", "Frenldy", "WTF", "Moms", "Dads", "Gental", "Stive", "Oh..A", "Fallen", "Fat", "Mr", "Miss", "Accurate", "Hard", "Soft", "Coffee", "Who?", "You!", "Mrs", "1..2..3", "Rolling", "Tom The", "One", "Hello", "Great", "Sexy", "Vegan", "Brave", "Shy", "Cool", "Poor", "Rich", "Fast", "Gummy", "Yummy", "Masked", "Unusual", "American", "Bisexual", "MLG", "Mlg", "lil", "Lil", "Canoodle", "Wabbit", "Bumbershoot", "German")
    second = ("Coder", "Hot", "Spider,", "Poop", "NO!", "Pasta", "Cat", "Sofa", "Genital", "Wait!", "Out", "Hello?", "Hitler", "Tank", "Delete", "But", "Fuck", "Vegan", "Man", "Hacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Killer", "Woman", "Programmer", "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper", "Quickscoper", "Sniper", "Hero", "miscarriage", "Nincompoop", "Fatuous")
    firrst = random.choice(first)
    seccond = random.choice(second)
    name = (firrst + " " + seccond)
    nameout.insert(0.0, name)


def window():
    global nameout
    root = tk.Tk()
    root.geometry("367x246")
    root.resizable(0, 0)
    root.title("Character-Name Generator")

    tx = tk.Label(root, text="Feel free to use the Name Generator. \n Enjoy this silly yet funny Generator")
    tx.place(x=80, y=35)

    nameout = tk.Text(root, height=1, width=27, relief=tk.GROOVE)
    nameout.place(x=75, y=150)
    nameout.config(state="normal")

    button = tk.Button(root, text="Generate", height=1, width=10, command=name_generator_Eng, relief=tk.GROOVE)
    button.place(x=150, y=100)

    root.mainloop()

window()