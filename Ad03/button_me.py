import Tkinter as tk
window =tk.Tk()

count  =0

def buttonClick():
	# print "Beep!"					#控制台显示文字
	# button.config(text ="Clicked")	#按钮文字改变
	global count
	count = count + 1
	button.config(text=str(count))

button = tk.Button(window, text="Click me!", command=buttonClick)
button.pack()
window.mainloop()