import tkinter as tk

root = tk.Tk()
root.title("Placing")
root.geometry("350x250")
root.resizable(0, 0)
#-The grid geometry manager uses the concepts of rows and columns to arrange the widgets.

line1 = tk.Label(text="Hello world.\n This is ... grid")
line1.grid(column="0", row="3")
#--Grid use column and row. row is the Horizontal plasment. column is the vertical plasment.

button1 = tk.Button(text="pack")
#---ipady and ipadx is the size of the button ipady is vertical size and ipadx is Horizontal size.
#----pady is the vertical plasment and padx is the Horizontal plasment.
button1.grid(ipady="10", ipadx="20", pady="20", padx="150")

button2 = tk.Button(text="pack")
#-----If the cell is large than the widget.
#------The stick option specifies which side the widget should stick to and how to distribute any extra space within the cell that is not taken up by the widget at its original size.
#-------you can use the following "NW" "N" "NE" "W" "CENTER" "E" "SW" "S" "SE" to set what side it will stick to.
#--------#NOTE! leaving (sticky="") empty will make it take the center by default
#---------The "n" will make it stick to the windows north or if there is a Lable it will stick to the north of the Lable if it's above it.

button2.grid(sticky="n")
#----------I personal don't recommend this way. it's better to go with "pack()" or for more accurate placement use "place()". play around with it for yourself and see what you think.
root.mainloop()
