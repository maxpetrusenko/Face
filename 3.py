from Tkinter import *

window = Tk()

Button1 = Label(window, text = "Name:")
Button2 = Label(window, text = "Password:")
name = Entry(window)
password = Entry(window)

Button1.grid(row = 0, sticky = E)
Button2.grid(row = 1, sticky = E)

name.grid(row=0, column = 1)
password.grid(row=1, column = 1)

check = Checkbutton(window, text = "check box")
check.grid(columnspan = 2)

window.mainloop()