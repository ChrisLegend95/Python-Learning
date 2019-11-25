import tkinter as tk

root = tk.Tk()
root.title("Placing")
root.geometry("350x250")
root.resizable(0, 0)
root.iconbitmap("Icon.ico")

line1 = tk.Label(text="Hello world.\n This is 100,X and 100,Y using Place")
line1.place(x=100, y=100)

button1 = tk.Button(text="x=100, y=50")
button1.place(x=100, y=50)

button2 = tk.Button(text="x=190, y=50")
button2.place(x=190, y=50)

root.mainloop()