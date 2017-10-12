# WORKSHEET 3 GUI-FOR GRGOBOT using tiNKTER
# Not Python 2 Compactible


import tkinter as tk
from grobot import*

bill=NewRobot("bill")

rcApp=tk.Tk()
rcApp.title(" Grid Robot-Control ")  # Title of the box

# to create buttons and place in tha GUI

rstButton = tk.Button( rcApp, text="Restart" , command = bill.init)
rstButton.pack( side=tk.TOP)


rgtButton =  tk.Button( rcApp, text="Right" , command = bill.right)
rgtButton.pack( side=tk.RIGHT)


lftButton = tk.Button( rcApp , text="Left" , command= bill.left)
lftButton.pack( side=tk.LEFT)


fwButton = tk.Button(rcApp , text="Forward" , command= bill.forward)
fwButton.pack()


bwButton = tk.Button ( rcApp , text="bill look" , command= bill.look)
bwButton.pack()


rcApp.mainloop()
