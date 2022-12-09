from tkinter import *
import tkinter as tk
import sqlite3
from sqlite3 import Error


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(':memory:')
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


FONT = ('Futura', 18, 'normal')


def add_wine():
    window.minsize(width=750, height=600)

    wine_search_button.destroy()
    wine_add_button.destroy()
    wine_delete_button.destroy()

    wine_add_name = Label(text='Wine Name:', font=FONT, fg='WHITE')
    wine_add_name.grid(row=1, column=0, padx=3, pady=3)
    wine_add_name.config(background='MAROON')
    wine_add_bar = Entry(width=80)
    wine_add_bar.grid(column=1, row=1, pady=3, padx=3)
    wine_add_bar.focus()

    wine_add_grape = Label(text='Varietal:', font=FONT, fg='WHITE')
    wine_add_grape.grid(row=2, column=0, padx=3, pady=3)
    wine_add_grape.config(background='MAROON')
    wine_grape_entry = Entry(width=80)
    wine_grape_entry.grid(column=1, row=2, padx=3, pady=3)

    wine_add_glass_price = Label(text='Glass Price:', font=FONT, fg='WHITE')
    wine_add_glass_price.grid(row=3, column=0, padx=3, pady=3)
    wine_add_glass_price.config(background='MAROON')
    wine_glass_entry = Entry(width=80)
    wine_glass_entry.grid(column=1, row=3, padx=3, pady=3)

    wine_add_bottle_price = Label(text='Bottle Price', font=FONT, fg='WHITE')
    wine_add_bottle_price.grid(row=4, column=0, padx=3, pady=3)
    wine_add_bottle_price.config(background='MAROON')
    wine_bottle_entry = Entry(width=80)
    wine_bottle_entry.grid(column=1, row=4, padx=3, pady=3)

    addition_button = Button(text="Add to Inventory!")
    addition_button.grid(column=1, row=5)
    addition_button.config(height=3, width=40)

    def add_to_database():
        pass


def search_wine():
    window.minsize(width=800, height=400)

    wine_search_button.destroy()
    wine_add_button.destroy()
    wine_delete_button.destroy()

    wine_add_name = Label(text='Wine Name:', font=FONT)
    wine_add_name.grid(row=1, column=0, padx=3, pady=3)
    wine_add_name.config(background='MAROON')
    wine_add_bar = Entry(width=100)
    wine_add_bar.grid(column=1, row=1, pady=3, padx=3)
    wine_add_bar.focus()

    wine_add_grape = Label(text='Varietal:', font=FONT)
    wine_add_grape.grid(row=2, column=0, padx=3, pady=3)
    wine_add_grape.config(background='MAROON')
    wine_grape_entry = Entry(width=100)
    wine_grape_entry.grid(column=1, row=2, padx=3, pady=3)

    wine_add_glass_price = Label(text='Glass Price:', font=FONT)
    wine_add_glass_price.grid(row=3, column=0, padx=3, pady=3)
    wine_add_glass_price.config(background='MAROON')
    wine_glass_entry = Entry(width=100)
    wine_glass_entry.grid(column=1, row=3, padx=3, pady=3)

    wine_add_bottle_price = Label(text='Bottle Price', font=FONT)
    wine_add_bottle_price.grid(row=4, column=0, padx=3, pady=3)
    wine_add_bottle_price.config(background='MAROON')
    wine_bottle_entry = Entry(width=100)
    wine_bottle_entry.grid(column=1, row=4, padx=3, pady=3)

    addition_button = Button(text="Add to Inventory!")
    addition_button.grid(column=1, row=5)
    addition_button.config(height=3, width=40)

    def add_to_database():
        pass


# Window Config ------------------------------------------------------
window = tk.Tk()
window.title('Wine Inventory')
window.minsize(width=750, height=400)
window.config(padx=10, pady=10, bg='MAROON')

# Logo Config ---------------------------------------------------------
canvas = Canvas(width=500, height=350, highlightthickness=0)
logo = PhotoImage(file='ezgif-4-6895a0ba48.png')
canvas.create_image(250, 175, image=logo)
canvas.grid(column=1, row=0)
canvas.config(background='MAROON')

# Wine Search Config ----------------------------------------------------
# wine_search = Label(text='Search Wine:', font=FONT)
# wine_search.grid(column=0, row=1)
# wine_search.config(background='MAROON')
# wine_search_entry = Entry(width=80)
# wine_search_entry.focus()
# wine_search_entry.grid(column=1, row=1, pady=2, padx=2)
wine_search_button = Button(text='Search', height=5, width=15, command=search_wine)
wine_search_button.grid(column=1, row=1, pady=2, padx=2)

# Wine Add Config -------------------------------------------------------
# wine_add = Label(text='Add Wine:', font=FONT)
# wine_add.grid(column=0, row=2)
# wine_add.config(background='MAROON')
# wine_add_entry = Entry(width=80)
# wine_add_entry.grid(column=1, row=2)
wine_add_button = Button(text='Add', width=15, height=5, command=add_wine)
wine_add_button.grid(column=0, row=1, pady=2)

# Wine Delete Config -----------------------------------------------------
# wine_delete = Label(text='86 a Wine:', font=FONT)
# wine_delete.grid(column=0, row=3)
# wine_delete.config(background='MAROON')
# wine_delete_entry = Entry(width=80)
# wine_delete_entry.grid(column=1, row=3)
wine_delete_button = Button(text='86', width=15, height=5)
wine_delete_button.grid(column=2, row=1, pady=2, padx=2)

window.mainloop()
