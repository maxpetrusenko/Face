from Tkinter import *

window = Tk()

topFrame = Frame(window)
topFrame.pack(side = TOP)
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "Button 1", fg = "Blue")
button2 = Button(topFrame, text = "Button 2", fg = "Blue")
button3 = Button(topFrame, text = "Button 3", fg = "Blue")

button4 = Button(bottomFrame, text = "Button 4", fg = "Blue",bg = "red")
button5 = Button(bottomFrame, text = "Button 5", fg = "Blue", bg = "red")

button1.pack(side = LEFT)
button2.pack(side = RIGHT)
button3.pack()
button4.pack(fill = Y)
button5.pack(fill = X)


window.mainloop() #keep it open