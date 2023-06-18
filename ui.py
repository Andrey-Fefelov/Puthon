import tkinter as tk

from main import y


def button_callback():
    label.config(text=y(text_input.get()))


root = tk.Tk()
root.title('Приложение')
root.geometry('250x100')

text_input = tk.Entry(root)
text_input.pack()

button = tk.Button(root, text='Старт', command=button_callback)
button.pack()

label = tk.Label(root, text='')
label.pack()

root.mainloop()
