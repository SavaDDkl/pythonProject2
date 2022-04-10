import tkinter as tk

def show_messadge(text):
    label.config(text=text)

def onclick():
    time = int(entry.get())
    if time < 0 or time > 23:
        show_messadge('Неккоректное время!')
        return
    if 5 <= time <= 12:
        show_messadge('Сейчас утро!')

    elif 13 <= time <= 16:
        show_messadge('Сейчас день!')

    elif 17 <= time <= 20:
        show_messadge('Сейчас вечер!')

    elif 21 <= time <= 23 or 0 <= time <= 4:
        show_messadge('Сейчас вечер!')

FONT = ('Comic Sans MS', 16)

window = tk.Tk()

entry = tk.Entry(font = FONT)
entry.pack(pady = 20)

btn = tk.Button(text = 'Узнать часть дня', command = onclick, font = FONT)
btn.pack(pady = 20)

label = tk.Label(text = 'Random text', font = FONT)
label.pack(pady = 20)

window.mainloop()