from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
from sqlite3 import Error
from wines import Wines

FONT = ('Futura', 18, 'normal')

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE wine (
                name text,
                grape text,
                region text,
                glass_price integer,
                bottle_price integer
                 )""")


def add_wine_screen():
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

    wine_add_region = Label(text='Region:', font=FONT, fg='WHITE')
    wine_add_region.grid(row=3, column=0, padx=3, pady=3)
    wine_add_region.config(background='MAROON')
    wine_region_entry = Entry(width=80)
    wine_region_entry.grid(column=1, row=3, padx=3, pady=3)

    wine_add_glass_price = Label(text='Glass Price:', font=FONT, fg='WHITE')
    wine_add_glass_price.grid(row=4, column=0, padx=3, pady=3)
    wine_add_glass_price.config(background='MAROON')
    wine_glass_entry = Entry(width=80)
    wine_glass_entry.grid(column=1, row=4, padx=3, pady=3)

    wine_add_bottle_price = Label(text='Bottle Price', font=FONT, fg='WHITE')
    wine_add_bottle_price.grid(row=5, column=0, padx=3, pady=3)
    wine_add_bottle_price.config(background='MAROON')
    wine_bottle_entry = Entry(width=80)
    wine_bottle_entry.grid(column=1, row=5, padx=3, pady=3)

    def add_to_database():
        wine_name = wine_add_bar.get()
        wine_grape = wine_grape_entry.get()
        wine_region = wine_region_entry.get()
        wine_glass_price = int(wine_glass_entry.get())
        wine_bottle_price = int(wine_bottle_entry.get())
        wine_info = [wine_name, wine_grape, wine_region, wine_glass_price, wine_bottle_price]
        if wine_info == '':
                messagebox.showinfo(title='Hol up', message='Please make sure all fields are filled out'
                                                                'and have something entered')
        try:

            else:
                with connection:
                    cursor.execute("INSERT INTO wine VALUES (:name, :grape, :region, :glass_price, :bottle_price)",
                                   {
                                       "name": wine_name, "grape": wine_grape, "region": wine_region,
                                       "glass_price": wine_glass_price, "bottle_price": wine_bottle_price
                                   })
                    cursor.execute("SELECT * FROM wine WHERE name=:name", {'name': wine_name})
                    result = cursor.fetchall()
                    print(result)
                    wine_add_name.destroy()
                    wine_add_bar.destroy()
                    wine_add_grape.destroy()
                    wine_grape_entry.destroy()
                    wine_add_region.destroy()
                    wine_region_entry.destroy()
                    wine_add_glass_price.destroy()
                    wine_glass_entry.destroy()
                    wine_add_bottle_price.destroy()
                    wine_bottle_entry.destroy()
                    addition_button.destroy()

                home_wine_search_button = Button(text='Search', height=5, width=15, command=search_wine)
                home_wine_search_button.grid(column=1, row=1, pady=2, padx=2)
                home_wine_add_button = Button(text='Add', width=15, height=5, command=add_wine_screen)
                home_wine_add_button.grid(column=0, row=1, pady=2)
                home_wine_delete_button = Button(text='86', width=15, height=5)
                home_wine_delete_button.grid(column=2, row=1, pady=2, padx=2)
                window.minsize(width=750, height=400)

            except ValueError:
                messagebox.showinfo(title='Error', message="Make sure you've entered a numerical value for the glass"
                                                           " and bottle prices")

    addition_button = Button(text="Add to Inventory!", command=add_to_database)
    addition_button.grid(column=1, row=6)
    addition_button.config(height=3, width=40)


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

# Home Screen Buttons -------------------------------------------------
wine_search_button = Button(text='Search', height=5, width=15, command=search_wine)
wine_search_button.grid(column=1, row=1, pady=2, padx=2)

wine_add_button = Button(text='Add', width=15, height=5, command=add_wine_screen)
wine_add_button.grid(column=0, row=1, pady=2)

wine_delete_button = Button(text='86', width=15, height=5)
wine_delete_button.grid(column=2, row=1, pady=2, padx=2)

window.mainloop()
