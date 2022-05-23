import tkinter as tk
from tkinter import ttk  # neuer Style von Funktion getrennt
import tkinter.font as tkfont
from tkinter.ttk import Radiobutton
from PIL import Image, ImageTk  # für Bilder in Labels


def text_input():
    textinput.set(entry1.get())


def set_option_label():
    textOption.set(option.get())


root = tk.Tk()
root.title('Python TKinter Beispiel Frame')
root.geometry("350x450")  # Size
root.minsize(width=250, height=250)  # min
root.maxsize(width=800, height=800)  # max
root.resizable(width=True, height=True)  # for no change of Size, set to False
font = tkfont.Font(size=20)

# side: 'bottom','left', 'right'
label1 = tk.Label(root, text='Textfeld', font=font)
label1.grid(row=0, columnspan=3)

# textinput field
entry1 = ttk.Entry(root, width=40)
entry1.grid(row=1, columnspan=2)
button1 = ttk.Button(root, text="Eingabe", command=text_input)
button1.grid(row=1, column=2)
textinput = tk.StringVar()
textinput.set(' ')
label2 = ttk.Label(root, textvariable=textinput)
label2.grid(row=2, columnspan=3)

# radiobutton
label3 = ttk.Label(root, text='Radiobuttons', font=font)
label3.grid(row=3, columnspan=3)
option = tk.StringVar()
radio1 = Radiobutton(root, text='Option 1', value='option 1', variable=option, command=set_option_label)
radio1.grid(row=4, column=0)
radio2 = Radiobutton(root, text='Option 2', value='option 2', variable=option, command=set_option_label)
radio2.grid(row=4, column=1)
radio3 = Radiobutton(root, text='Option 3', value='option 3', variable=option, command=set_option_label)
radio3.grid(row=4, column=2)

textOption = tk.StringVar()
textOption.set(' ')
label4 = ttk.Label(root, textvariable=textOption)
label4.grid(row=6, columnspan=3)

# image in frame
label5 = ttk.Label(root, text='Bildbereich', font=font)
label5.grid(row=7, columnspan=3)
image = Image.open('img/th.jpg').resize(size=(50, 50))  # über .resize() Größe setzen
photo = ImageTk.PhotoImage(image)
labelIm = ttk.Label(root, image=photo, compound='bottom')
labelIm.grid(row=8, columnspan=3)

# combobox to choose one item
textCombo = tk.StringVar()
textCombo.set(' ')

label6 = ttk.Label(root, text='Auswahlbox', font=font)
label6.grid(row=9, columnspan=3)
combo = ttk.Combobox(root, values=['Auswahl 1', 'Auswahl 2', 'Auswahl 3'], textvariable=textCombo)
combo.grid(row=10, columnspan=3)
combo.current(0)
combo.bind()

label7 = ttk.Label(root, textvariable=textCombo)
label7.grid(row=11, columnspan=3)

# checkbox
label8 = ttk.Label(root, text='Checkbox', font=font)
label8.grid(row=12, columnspan=3)
checkboxValue = tk.StringVar()
checkboxValue.set(None)
checkbox = tk.Checkbutton(root, text='Checkbox', variable=checkboxValue, onvalue=1, offvalue=0)
checkbox.grid(row=13, columnspan=3)
checkboxLabel = tk.Label(root, textvariable=checkboxValue)
checkboxLabel.grid(row=14, columnspan=3)

# for item in label5.keys():
#     print(item, ': ', label5[item])

# mit configure methode kann einiges geändert werden
# Variable['Schlüssel'] können diese verändert werden
# .keys() gibt mögliche Keys des Widgets

# compound bestimmt Position relativ zum Text falls beides drin

root.mainloop()
