import Tkinter as tk
window = tk.Tk()

def checkPassword():
	password = "Oranges"
	enteredPassword = passwordEntry.get()
	if password == enteredPassword:
		confirmLable.config(text="Correct")
	else:
		confirmLable.config(text="Incorrect")

passwordLabel = tk.Label(window, text="password:")
passwordEntry = tk.Entry(window, show="*")

button = tk.Button(window, text="Enter", command=checkPassword)
confirmLable = tk.Label(window)

passwordLabel.pack()
passwordEntry.pack()
button.pack()
confirmLable.pack()

window.mainloop()