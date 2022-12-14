from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

FONT = ('Futura', 18, 'normal')

connection = sqlite3.connect('wine_db')
cursor = connection.cursor()


# cursor.execute("""CREATE TABLE wine (
#                 name text,
#                 grape text,
#                 vintage integer,
#                 on_hand integer,
#                 bottle_price integer
#                  )""")


def back_to_home():
    window.destroy()
    # window_new = tk.Tk()
    # window_new.title('Wine Inventory')
    # window_new.minsize(width=750, height=400)
    # window_new.config(padx=10, pady=10, bg='MAROON')
    #
    # # Logo Config ---------------------------------------------------------
    # canvas_new = Canvas(width=500, height=350, highlightthickness=0)
    # logo_new = PhotoImage(file='ezgif-4-6895a0ba48.png')
    # canvas_new.create_image(250, 175, image=logo_new)
    # canvas_new.grid(column=1, row=0)
    # canvas_new.config(background='MAROON')
    #
    # # Home Screen Buttons -------------------------------------------------
    # wine_search_button_new = Button(text='Search', height=5, width=15, command=search_wines_screen)
    # wine_search_button_new.grid(column=1, row=1, pady=2, padx=2)
    #
    # wine_add_button_new = Button(text='Add', width=15, height=5, command=add_wine_screen)
    # wine_add_button_new.grid(column=0, row=1, pady=2)
    #
    # wine_delete_button_new = Button(text='86', width=15, height=5, command=delete_wines_screen)
    # wine_delete_button_new.grid(column=2, row=1, pady=2, padx=2)


def add_wine_screen():
    window.minsize(width=750, height=625)
    window.maxsize(width=750, height=725)

    wine_search_button.destroy()
    wine_add_button.destroy()
    wine_delete_button.destroy()

    wine_add_name = Label(text='Wine Name:', font=FONT, fg='WHITE')
    wine_add_name.grid(row=1, column=0, padx=3, pady=3)
    wine_add_name.config(background='MAROON')
    wine_name_entry = Entry(width=80)
    wine_name_entry.grid(column=1, row=1, pady=3, padx=3)
    wine_name_entry.focus()

    wine_add_grape = Label(text='Varietal:', font=FONT, fg='WHITE')
    wine_add_grape.grid(row=2, column=0, padx=3, pady=3)
    wine_add_grape.config(background='MAROON')
    wine_grape_entry = Entry(width=80)
    wine_grape_entry.grid(column=1, row=2, padx=3, pady=3)

    wine_vintage_entry = Label(text='Vintage:', font=FONT, fg='WHITE')
    wine_vintage_entry.grid(row=3, column=0, padx=3, pady=3)
    wine_vintage_entry.config(background='MAROON')
    wine_vintage_add = Entry(width=80)
    wine_vintage_add.grid(column=1, row=3, pady=3, padx=3)

    wine_inventory_on_hand = Label(text='Bottles on Hand:', font=FONT, fg='WHITE')
    wine_inventory_on_hand.grid(row=4, column=0, padx=3, pady=3)
    wine_inventory_on_hand.config(background='MAROON')
    wine_on_hand_entry = Entry(width=80)
    wine_on_hand_entry.grid(column=1, row=4, padx=3, pady=3)

    wine_add_bottle_price = Label(text='Bottle Price', font=FONT, fg='WHITE')
    wine_add_bottle_price.grid(row=5, column=0, padx=3, pady=3)
    wine_add_bottle_price.config(background='MAROON')
    wine_bottle_entry = Entry(width=80)
    wine_bottle_entry.grid(column=1, row=5, padx=3, pady=3)

    def add_to_database():
        try:
            wine_name = wine_name_entry.get()
            wine_grape = wine_grape_entry.get()
            wine_vintage = wine_vintage_add.get()
            wine_on_hand = wine_on_hand_entry.get()
            wine_bottle_price = int(wine_bottle_entry.get())
            wine_info = (wine_name, wine_grape, wine_bottle_price)
            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')
            else:
                with connection:
                    cursor.execute("INSERT INTO wine VALUES (:name, :grape, :vintage :bottle_price, :on_hand)",
                                   {
                                       "name": wine_name, "grape": wine_grape, "on_hand": wine_on_hand,
                                       'vintage': wine_vintage, "bottle_price": wine_bottle_price
                                   })
                wine_name_entry.delete(0, END)
                wine_grape_entry.delete(0, END)
                wine_vintage_add.delete(0, END)
                wine_on_hand_entry.delete(0, END)
                wine_bottle_entry.delete(0, END)

        except ValueError:
            messagebox.showinfo(title='Wait a second', message='Make sure you are entering numbers for the bottle '
                                                               'prices, inventory on hand and filled out every field!')

    addition_button = Button(text="Add to Inventory!", command=add_to_database)
    addition_button.grid(column=1, row=6)
    addition_button.config(height=3, width=40)

    back_button = Button(text='Back to Home', command=back_to_home)
    back_button.grid(column=0, row=6)


def search_wines_screen():
    window.minsize(width=750, height=625)
    window.maxsize(width=750, height=625)

    wine_search_button.destroy()
    wine_add_button.destroy()
    wine_delete_button.destroy()

    wine_add_name = Label(text='Wine Name:', font=FONT, fg='WHITE')
    wine_add_name.grid(row=1, column=0, padx=3, pady=3)
    wine_add_name.config(background='MAROON')
    wine_name_entry = Entry(width=80)
    wine_name_entry.grid(column=1, row=1, pady=3, padx=3)
    wine_name_entry.focus()

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

    def search_wines():
        try:
            wine_name = wine_name_entry.get()
            wine_grape = wine_grape_entry.get()
            wine_region = wine_region_entry.get()
            wine_glass_price = int(wine_glass_entry.get())
            wine_bottle_price = int(wine_bottle_entry.get())
            wine_info = (wine_name, wine_grape, wine_region, wine_glass_price, wine_bottle_price)
            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')
            else:
                with connection:
                    cursor.execute("INSERT INTO wine VALUES (:name, :grape, :region, :glass_price, :bottle_price)",
                                   {
                                       "name": wine_name, "grape": wine_grape, "region": wine_region,
                                       "glass_price": wine_glass_price, "bottle_price": wine_bottle_price
                                   })
                wine_name_entry.delete(0, END)
                wine_grape_entry.delete(0, END)
                wine_region_entry.delete(0, END)
                wine_glass_entry.delete(0, END)
                wine_bottle_entry.delete(0, END)

        except ValueError:
            messagebox.showinfo(title='Wait a second', message='Make sure you are entering numbers for the glass'
                                                               ' and bottle prices!')

    single_search_button = Button(text="Search single wine", command=search_wines)
    single_search_button.grid(column=0, row=6)
    single_search_button.config(height=3, width=20)

    multiple_search_button = Button(text="Search multiple wines")
    multiple_search_button.grid(column=1, row=6)
    multiple_search_button.config(height=3, width=20, pady=5, padx=5)

    home_button = Button(text='Go Back')
    home_button.grid(column=0, row=0)
    home_button.config(height=3, width=10)


def delete_wines_screen():
    window.minsize(width=750, height=425)
    window.maxsize(width=750, height=525)

    wine_search_button.destroy()
    wine_add_button.destroy()
    wine_delete_button.destroy()

    wine_add_name = Label(text='Wine Name:', font=FONT, fg='WHITE')
    wine_add_name.grid(row=1, column=0, padx=3, pady=3)
    wine_add_name.config(background='MAROON')
    wine_name_entry = Entry(width=80)
    wine_name_entry.grid(column=1, row=1, pady=3, padx=3)
    wine_name_entry.focus()

    wine_add_vintage = Label(text='Vintage:', font=FONT, fg='WHITE')
    wine_add_vintage.grid(row=4, column=0, padx=3, pady=3)
    wine_add_vintage.config(background='MAROON')
    wine_vintage_add = Entry(width=80)
    wine_vintage_add.grid(column=1, row=4, pady=3, padx=3)

    def remove_from_database():
        try:
            wine_name = wine_name_entry.get()
            wine_vintage = int(wine_vintage_add.get())
            wine_info = (wine_name, wine_vintage)
            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')
            else:
                with connection:
                    answer = messagebox.askyesno(title='Confirmation', message=f"Are you sure you want to delete "
                                                                               f"{wine_name}, Vintage: {wine_vintage}"
                                                                               f" from the database?")
                    if answer:
                        cursor.execute("DELETE from wine WHERE name = :name AND vintage = :vintage",
                                       {'name': wine_name, 'vintage': wine_vintage})
                        messagebox.showinfo(title="Completed", message=f"{wine_name} has been successfully removed.")
                    else:
                        print(answer)
                        messagebox.showinfo(title='', message='Okay')
                wine_name_entry.delete(0, END)
                wine_vintage_add.delete(0, END)
                wine_name_entry.focus()

        except ValueError:
            messagebox.showerror(title='Vintage', message='Make sure you are entering a numerical value for the '
                                                          'vintage!')

    addition_button = Button(text="Remove from Inventory", command=remove_from_database)
    addition_button.grid(column=1, row=7)
    addition_button.config(height=3, width=40)

    back_button = Button(text='Back to Home', command=back_to_home)
    back_button.grid(column=0, row=7)


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
wine_search_button = Button(text='Search', height=5, width=15, command=search_wines_screen)
wine_search_button.grid(column=1, row=1, pady=2, padx=2)

wine_add_button = Button(text='Add', width=15, height=5, command=add_wine_screen)
wine_add_button.grid(column=0, row=1, pady=2)

wine_delete_button = Button(text='86', width=15, height=5, command=delete_wines_screen)
wine_delete_button.grid(column=2, row=1, pady=2, padx=2)


# def search():
#     cursor.execute("SELECT * FROM wine WHERE")
#     return cursor.fetchall()
#
#
# print(search())
# print(window.winfo_children())

window.mainloop()
