import tkinter as tk

def show_messadge(number):
    label.config(text=number)

def onclick():
    if entry.get() == '':
        show_messadge('Пустое поле!')
        return
    if entry1.get() == '':
        show_messadge('Пустое поле!')
        return
    a = int(entry.get())

    b = int(entry1.get())

    show_messadge(str(a + b))

def w():
    if entry.get() == '':
        show_messadge('Пустое поле!')
        return
    if entry1.get() == '':
        show_messadge('Пустое поле!')
        return
    a = int(entry.get())

    b = int(entry1.get())

    show_messadge(str(a - b))

def q():
    if entry.get() == '':
        show_messadge('Пустое поле!')
        return
    if entry1.get() == '':
        show_messadge('Пустое поле!')
        return
    a = int(entry.get())

    b = int(entry1.get())

    show_messadge(str(a * b))

def e():
    if entry.get() == '':
        show_messadge('Пустое поле!')
        return
    if entry1.get() == '':
        show_messadge('Пустое поле!')
        return

    a = int(entry.get())

    b = int(entry1.get())

    if b == 0:
        show_messadge('Делить на 0 нельзя!')
        return
    show_messadge(str(a / b))


FONT = ('Comic Sans MS', 16)

window = tk.Tk()

entry = tk.Entry(font = FONT)
entry.pack(pady = 20)
entry1 = tk.Entry(font = FONT)
entry1.pack(pady = 20)

btn = tk.Button(text = '+', command = onclick, font = FONT)
btn.pack(pady = 20)

btn2 = tk.Button(text = '-', command = q, font = FONT)
btn2.pack(pady = 20)

btn3 = tk.Button(text = '*', command = w, font = FONT)
btn3.pack(pady = 20)

btn4 = tk.Button(text = '/', command = e, font = FONT)
btn4.pack(pady = 20)

label = tk.Label(text = 'Random text', font = FONT)
label.pack(pady = 20)

window.mainloop()