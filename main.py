from tkinter import *
import tkinter as tk
from screeninfo import get_monitors
# import sqlite3
# from sqlite3 import Error
#
#
# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect('Wine Inventory.db')
#         print("Connection to SQLite DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#     return connection


FONT = ('Futura', 18, 'bold')


app_width = 0
app_height = 0

for m in get_monitors():
    if m.__getattribute__('is_primary'):
        app_width = (m.__getattribute__('width')) * .25
        app_height = (m.__getattribute__('height')) * .25


def add_wine():
    canvas.delete('all')
    wine_search.destroy()
    window.minsize(width=900, height=900)
    fuck = Label(text='FUCK')


# Window Config ------------------------------------------------------
window = tk.Tk()
window.title('Wine Inventory')
window.minsize(width=int(app_width), height=int(app_height))
window.config(padx=10, pady=10, bg='MAROON')

# Logo Config ---------------------------------------------------------
canvas = Canvas(width=app_width, height=app_height, highlightthickness=0)
logo = PhotoImage(file='ezgif-4-6895a0ba48.png')
canvas.create_image(200, 130, image=logo)
canvas.grid(column=1, row=0)
canvas.config(background='MAROON')

# Wine Search Config ----------------------------------------------------
wine_search = Label(text='Search Wine:', font=FONT)
wine_search.grid(column=0, row=1)
wine_search.config(background='MAROON')
wine_search_entry = Entry(width=80)
wine_search_entry.focus()
wine_search_entry.grid(column=1, row=1, pady=2, padx=2)
wine_search_button = Button(text='Search', command=add_wine)
wine_search_button.grid(column=2, row=1, pady=2, padx=2)

# Wine Add Config -------------------------------------------------------
wine_add = Label(text='Add Wine:', font=FONT)
wine_add.grid(column=0, row=2)
wine_add.config(background='MAROON')
wine_add_entry = Entry(width=80)
wine_add_entry.grid(column=1, row=2)
wine_add_button = Button(text='Add')
wine_add_button.grid(column=2, row=2, pady=2)

# Wine Delete Config -----------------------------------------------------
wine_delete = Label(text='86 a Wine:', font=FONT)
wine_delete.grid(column=0, row=3)
wine_delete.config(background='MAROON')
wine_delete_entry = Entry(width=80)
wine_delete_entry.grid(column=1, row=3)
wine_search_button = Button(text='86')
wine_search_button.grid(column=2, row=3, pady=2, padx=2)

window.mainloop()
