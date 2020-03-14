from tkinter import *

root = Tk() #make a window 

root.geometry("500x500")  #set window to specific size 

display = Entry(root, font=('Ariel', 24), justify=RIGHT)
display.grid(row=0, column=0, columnspan=5)

#Make window before defining functions

def greeting():
  print("Hello World")

#Make functions before creating buttons 

hw_btn = Button(root, text="Hello", command=greeting) #creates a button
hw_btn.grid(row=1, column=0) #places button in the window 


root.mainloop() # starts event loop last line 