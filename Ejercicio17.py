import tkinter as tk

window = tk.Tk()

# Create a StringVar to store the text displayed on the label
display_text = tk.StringVar()

# Create a label to display the text
display = tk.Label(window, textvariable=display_text)

# Set the initial text to be displayed on the label
display_text.set("0")

# Place the label on the window
display.grid(row=0, column=0, columnspan=3)

# Create the buttons
button1 = tk.Button(window, text="1")
button2 = tk.Button(window, text="2")
button3 = tk.Button(window, text="3")
button4 = tk.Button(window, text="4")
button5 = tk.Button(window, text="5")
button6 = tk.Button(window, text="6")
button7 = tk.Button(window, text="7")
button8 = tk.Button(window, text="8")
button9 = tk.Button(window, text="9")

# Colocamos los botones en la ventana
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

window.mainloop()
