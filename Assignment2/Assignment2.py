import tkinter as tk
import tkinter.messagebox as msg
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Simple Calculator')
window.configure(bg='lightgray')

frame = tk.Frame(master=window, bg="lightgray", padx=10, pady=10)
frame.pack()

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=35, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, ipady=5, pady=5)

def button_click(number):
    entry.insert(tk.END, number)

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        msg.showerror("Error", "Invalid Input")

def clear_entry():
    entry.delete(0, tk.END)

button_params = {'padx': 15, 'pady': 10, 'width': 4, 'font': ('Arial', 12), 'bg': 'white'}

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1)
]

for (text, row, col) in buttons:
    tk.Button(master=frame, text=text, command=lambda t=text: button_click(t), **button_params).grid(row=row, column=col, pady=5)

operators = [
    ('+', 4, 0), ('-', 4, 2),
    ('*', 5, 0), ('/', 5, 2)
]

for (text, row, col) in operators:
    tk.Button(master=frame, text=text, command=lambda t=text: button_click(t), **button_params).grid(row=row, column=col, pady=5)

tk.Button(master=frame, text='C', command=clear_entry, padx=15, pady=10, width=4, font=('Arial', 12), bg='lightcoral').grid(row=5, column=1, pady=5)
tk.Button(master=frame, text='=', command=calculate, padx=15, pady=10, width=17, font=('Arial', 12), bg='lightgreen').grid(row=6, column=0, columnspan=3, pady=5)

window.mainloop()
