from tkinter import *
from tkinter import ttk #-----ttk is not needed for this at all. however, if you remove ttk you must config the rest of widgets back to normal tk.
import time


#This function is repeated and updating the progressbar and text in % for us.
def step():
    for i in range(25): #-----i in range of 25 meaning it will count untill value in the progressbar have reach 25 in value.
        window.update_idletasks() #-----This keeps the windows updated so we can see the progressbar moving without it... nothing would move on the progressbar but it still update in next step.
        loading["value"] += 1 #--------Adds 1+ to are progressbar value so from 0 to 1
        time.sleep(0.05) #-----This adds a deley for simulating a loading so 0.05 ms
        bar["text"]=loading["value"],'%' #-----This update the progressbar value and the label with the value of % showing next to the bar in the gui.
        info_check.config(text="Loading program...") #----------Just a small information on what happens [! !NOTE! It's fake messages. you can change it to anything. !]
    info_check.update() #------Updating the information so it's ready to run again. Mostly so we not get left with Label text in the back of the current one showing.
    loading["value"] = 25 #------Making sure the value is correct before moving on. same with the loading text that show progressbar value in %
    bar["text"]=loading["value"],"%"
    step2() #-------Now running step2 wich is just the same almost

def step2():
    for i in range(25): #----So This will stay 25 in range sense we go to 100 we devide 100 by 4 and get 25 for each task. This is not the only way you can do this on.
        window.update_idletasks()
        info_check.update()
        loading["value"] += 1
        time.sleep(0.15)
        info_check.config(text="Installing second party tools...")
        bar["text"]=loading["value"],"%"
    loading["value"] = 50 #-------Note the value is 50 but in range was 25? Thats because we need to add 25 for each step it make so we not going over board on the progressbar.
    bar["text"]=loading["value"],"%"
    step3()

def step3():
    for i in range(25):
        window.update_idletasks()
        info_check.update()
        loading["value"] += 1
        time.sleep(0.25)
        info_check.config(text="Removing system files....")
        bar["text"]=loading["value"],"%"
    loading["value"] = 75
    bar["text"]=loading["value"],"%"
    step4()

def step4():
    window.update_idletasks()
    for i in range(25):
        window.update_idletasks()
        info_check.update()
        loading["value"] += 1
        time.sleep(0.20)
        info_check.config(text="Running Virus...")
        bar["text"]=loading["value"],"%"
    info_check.config(text="Done!")
    quit
#----Short note to get to 100% we devide this in 4 so it's 25% for each task. so when you see the value getting set to 50, 75 it's becuse we add 25 for all the 4 steps
#----------------------- so Step 1 is 25 in value then when it moves over to step 2 we don't need to add 25 more to the value untill the end of the step so after step2 the value is set to 50 then step 3 +25 75 then step 4 + 25 = 100
window = Tk() #------Just the main window.
window.title("Don't panik")
window.geometry("500x300")
window.config(bg="light grey")

can = Canvas(window, bg="dark blue", width=500, height=80) #------Not needed just for show.
can.place(x=-2, y=-2)

thi = Label(can, text="Welcome to \n Test of Progressbar", fg="white", bg="dark blue", font=("Arial", 25)) #------Not needed just for show.
thi.place(x=110, y=0)

#------ttk.Style for ttk button.------------------------------------------------------------
s = ttk.Style()
s.configure("JS.TButton", font=("Helvetica", 12), background="light grey", foreground="black")
#------------------------------------------------------------------------------------
#-------------Tk button that start the functions of the progressbar and calling for the step (1)
#-------------------------------------------------------------------------------------
button = ttk.Button(window, text="Install", command=step, style="JS.TButton")
button.place(x=210, y=145)

#///////------Here is most things that is showing on the gui for the progressbar and text----////////
loading = ttk.Progressbar(window, length=100, value=0, mode='determinate', orient="horizontal")#---Progressbar
loading.place(x=130, y=200, width=250)

info_check = Label(window, text="asddassda", bg="light grey")#---Label with text that get updated.
info_check.place(x=130, y=175)

bar = Label(window, text="0%", bg="light grey")#---Label with % track of are progressbar steps and progress value.
bar.place(x=100, y=200)

window.mainloop() #---Mainloop making sure the window is running in loop.
