import random #--Importing random for picking something random from the lists.
#--NOTE!! "import random" is not a part of tkinter, this is just for making a program simple and easy to test and play around with.
import tkinter as tk
#--This is the function that creates a different name by using random for picking from "first" and "second" containers that hold Variables.
def name_generator_Eng():
    nameout.delete(1.0,"end") #--This is to clear the text in the "nameout" (tk.Text)
    #---Here is a bind named "first" and it contains Variables. It's possible to add as much as you want to this by going to the end and type ("German", "New name", "new name")
    #---Same goes for the second. It uses a bind to a container with Variables.
    first = ("Super", "Retarded", "Shit", "Frenldy", "WTF", "Moms", "Dads", "Gental", "Stive", "Oh..A", "Fallen", "Fat", "Mr", "Miss", "Accurate", "Hard", "Soft", "Coffee", "Who?", "You!", "Mrs", "1..2..3", "Rolling", "Tom The", "One", "Hello", "Great", "Sexy", "Vegan", "Brave", "Shy", "Cool", "Poor", "Rich", "Fast", "Gummy", "Yummy", "Masked", "Unusual", "American", "Bisexual", "MLG", "Mlg", "lil", "Lil", "Canoodle", "Wabbit", "Bumbershoot", "German")
    second = ("Coder", "Hot", "Spider,", "Poop", "NO!", "Pasta", "Cat", "Sofa", "Genital", "Wait!", "Out", "Hello?", "Hitler", "Tank", "Delete", "But", "Fuck", "Vegan", "Man", "Hacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Killer", "Woman", "Programmer", "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper", "Quickscoper", "Sniper", "Hero", "miscarriage", "Nincompoop", "Fatuous")
    firrst = random.choice(first) #---Here we sign firrst to random with the option "choice(first)". This will go on through the container of "first" and pick a random Variables.
    seccond = random.choice(second)#--And here we sign seccond to random with option "choice(second)". This will also go through teh list and grab a random Variables
    name = (firrst + " " + seccond) #----This combind the "firrst" and "seccond". It's binded to "name" wish is used on function "window():" and it must be (firrst + "" + seccond) for it to combind with a space in between the Variables.
    nameout.insert(0.0, name) #---This will generate the random name it got from the option random.choice.
    #---"nameout.insert" will put the "name" from this function to the othere function "window():" by communicating with the global keyword "nameout".
    #---With global keyword "nameout", we can accsess the options of that tool in othere functions. Right now nameout is the only global keyword we can use (The only keyword we have given accsess to.)

#--function "window():" is the main window of the program. Function "name_generator_Eng():" is another function but with only a script to create are random name.
def window():
    global nameout #--Global keyword. This is used for othere function can grab the keyword and use it in it's own function.
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
    #--This is a mainloop. It keeps the window running and it's needed if you want to see a window from tkinter.
    root.mainloop()
#---This starts teh function "window():" This is needed to run the program.
window()
