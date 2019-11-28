import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("250x400")
root.title("Tkinter window")
root.resizable(0, 0)

bt = tk.ttk.Button(root, text="ttk button")
bt.place(x=50, y=40)

bt2 = tk.Button(root, text="tk button")
bt2.place(x=150, y=40)

lb = tk.ttk.Label(text="ttk Label")
lb.place(x=50, y=80)

lb2 = tk.Label(text="tk Label")
lb2.place(x=150, y=80)

ent = tk.ttk.Entry(width=10)
ent.place(x=50, y=100)

ent2 = tk.Entry(width=10)
ent2.place(x=150, y=100)

rdb = tk.ttk.Radiobutton(text="ttk Radiobutton")
rdb.place(x=20, y=130)

rdb2 = tk.Radiobutton(text="tk Radiobutton")
rdb2.place(x=130, y=130)

ck = tk.ttk.Checkbutton(text="ttk Checkbutton")
ck.place(x=20, y=160)

ck2 = tk.Checkbutton(text="tk Checkbutton")
ck2.place(x=130, y=160)

sp = tk.ttk.Spinbox(root, width=12)
sp.place(x=20, y=200)

sp2 = tk.Spinbox(root, width=12)
sp2.place(x=130, y=200)

root.mainloop()