import tkinter as tk

root = tk.Tk()
root.title("Placing")
root.geometry("350x250")
root.resizable(0, 0)

line1 = tk.Label(text="Hello world.\n This is ... pack")
line1.pack()

button1 = tk.Button(text="pack")
button1.pack(anchor="nw")

button2 = tk.Button(text="pack")
button2.pack(side="bottom")
#-----must be -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side in pack(anchor="center")

root.mainloop()