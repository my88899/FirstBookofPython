import Tkinter as tk
window = tk.Tk()


def sliderUpdat(source):
    red = redSlinder.get()
    green = greenSlinder.get()
    blue = blueSlinder.get()

    colour = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg=colour)

    hexText.delete(0, tk.END)
    hexText.insert(0, colour)

redSlinder = tk.Scale(window, from_=0, to=255, command=sliderUpdat)
greenSlinder = tk.Scale(window, from_=0, to=255, command=sliderUpdat)
blueSlinder = tk.Scale(window, from_=0, to=255, command=sliderUpdat)
canvas = tk.Canvas(window, height=200, width=200)
hexText = tk.Entry(window)

redSlinder.grid(row=1, column=1)
greenSlinder.grid(row=1, column=2)
blueSlinder.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
hexText.grid(row=3, column=1, columnspan=3)

tk.mainloop()
