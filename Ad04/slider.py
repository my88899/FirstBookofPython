import Tkinter as tk
window=tk.Tk()

redDirection ="up"
greenDirection ="up"
blueDirextion ="up"

red =0
green=0
blue=0

def colourUpdate():
	global red
	global green
	global blue

	global redDirection
	global greenDirection
	global blueDirextion
	
	redIncrement =redSlider.get()
	greenIncrement =greenSlider.get()
	blueIncrement =blueSlider.get()


window.mainloop()