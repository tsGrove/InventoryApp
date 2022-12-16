import os.path
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

FONT = ('Futura', 18, 'normal')
connection = sqlite3.connect('wine')
cursor = connection.cursor()

#
# cursor.execute("""CREATE TABLE wine (
#                 name text,
#                 grape text,
#                 vintage integer,
#                 on_hand integer,
#                 bottle_price integer
#                  )""")


def back_to_home():
    window.destroy()


def add_wine_screen():
    window.minsize(width=750, height=625)

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

    wine_add_bottle_price = Label(text='Bottle Price:', font=FONT, fg='WHITE')
    wine_add_bottle_price.grid(row=5, column=0, padx=3, pady=3)
    wine_add_bottle_price.config(background='MAROON')
    wine_bottle_entry = Entry(width=80)
    wine_bottle_entry.grid(column=1, row=5, padx=3, pady=3)

    def add_to_database():
        try:
            wine_name = wine_name_entry.get().title()
            wine_grape = wine_grape_entry.get().title()
            wine_vintage = int(wine_vintage_add.get().title())
            wine_on_hand = int(wine_on_hand_entry.get())
            wine_bottle_price = int(wine_bottle_entry.get())
            wine_info = (wine_name, wine_grape, wine_bottle_price)
            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')
            else:
                with connection:
                    cursor.execute("SELECT * FROM wine WHERE name =:name AND vintage =:vintage",
                                   {
                                       'name': wine_name,
                                       'vintage': wine_vintage
                                   })
                    wine = cursor.fetchone()
                    print(wine)
                    if wine is None:
                        cursor.execute("INSERT INTO wine VALUES (:name, :grape, :vintage, :on_hand, :bottle_price)",
                                       {
                                           "name": wine_name, "grape": wine_grape, "on_hand": wine_on_hand,
                                           'vintage': wine_vintage, "bottle_price": wine_bottle_price
                                       })
                        messagebox.showinfo(title='Successful', message=f'{wine_name} has successfully been added '
                                                                        f'to the database!')
                    else:
                        messagebox.showerror(title="Uh-oh", message="It would appear that that wine is already "
                                                                    "in the database!")
                wine_name_entry.delete(0, END)
                wine_grape_entry.delete(0, END)
                wine_vintage_add.delete(0, END)
                wine_on_hand_entry.delete(0, END)
                wine_bottle_entry.delete(0, END)
                wine_name_entry.focus()

        except ValueError:
            messagebox.showinfo(title='Wait a second', message='Make sure every field is filled out and you are'
                                                               ' entering numbers for the vintage, bottles on hand'
                                                               ' and bottle prices!')

    addition_button = Button(text="Add to Inventory!", command=add_to_database)
    addition_button.grid(column=1, row=6)
    addition_button.config(height=3, width=40)

    back_button = Button(text='Back to Home', command=back_to_home)
    back_button.grid(column=0, row=0)


def search_wines_screen():
    window.minsize(width=750, height=425)

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
    wine_add_vintage.grid(row=2, column=0, padx=3, pady=3)
    wine_add_vintage.config(background='MAROON')
    wine_vintage_add = Entry(width=80)
    wine_vintage_add.grid(column=1, row=2, pady=3, padx=3)

    wine_bottle_update = Label(text='Bottles on Hand:', font=FONT, fg='WHITE')
    wine_bottle_update.grid(row=3, column=0, padx=3, pady=3)
    wine_bottle_update.config(background='MAROON')
    wine_bottle_update_add = Entry(width=80)
    wine_bottle_update_add.grid(column=1, row=3, pady=3, padx=3)

    def search_wines():
        try:
            wine_name = wine_name_entry.get().title()
            wine_vintage = int(wine_vintage_add.get())
            wine_info = (wine_name, wine_vintage)
            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')
            else:
                with connection:
                    cursor.execute("SELECT * FROM wine WHERE name =:name AND vintage =:vintage",
                                   {
                                       'name': wine_name,
                                       'vintage': wine_vintage
                                   })
                    wine = cursor.fetchone()
                    print(wine)
                    if wine is not None:
                        messagebox.showinfo(title='Info', message=f'Name: {wine[0]}, Varietal: {wine[1]}, '
                                                                  f'Vintage: {wine[2]},\n '
                                                                  f'Bottles on Hand: {wine[3]}, '
                                                                  f'Bottle Price: {wine[4]}')
                        wine_name_entry.delete(0, END)
                        wine_vintage_add.delete(0, END)
                        wine_name_entry.focus()
                    else:
                        messagebox.showerror(title='Uh-oh', message="Sorry, looks like that wine"
                                                                    " isn't in the database!")
                        wine_name_entry.focus()
        except ValueError:
            messagebox.showinfo(title='Wait a second', message='Make sure all the fields are filled out and you are'
                                                               ' entering numerical values for the vintage!')

    def search_every_wine():
        base = os.path.dirname(os.path.abspath('main.py'))
        print(base)
        db_path = os.path.join(base, "PupilPremiumTable.db")
        with sqlite3.connect(db_path) as _:
            sqlite_select_query = f"""SELECT * from {db_path}"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print(records)

    def update_counts():
        try:
            wine_name = wine_name_entry.get().title()
            wine_vintage = int(wine_vintage_add.get())
            wine_bottle_updated_count = int(wine_bottle_update_add.get())
            wine_info = (wine_name, wine_vintage, wine_bottle_updated_count)
            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')
            else:
                with connection:
                    cursor.execute("SELECT * FROM wine WHERE name =:name AND vintage =:vintage",
                                   {
                                       'name': wine_name,
                                       'vintage': wine_vintage
                                   })
                    wine = cursor.fetchone()
                    if wine is not None:
                        cursor.execute("""UPDATE wine SET on_hand =:on_hand
                                        WHERE name =:name AND vintage =:vintage""",
                                       {
                                           'name': wine_name, 'vintage': wine_vintage,
                                           'on_hand': wine_bottle_updated_count
                                       })
                        messagebox.showinfo(title='Success', message=f"Bottle count successfully updated to"
                                                                     f" {wine_bottle_updated_count}!")
                        wine_name_entry.delete(0, END)
                        wine_vintage_add.delete(0, END)
                        wine_bottle_update_add.delete(0, END)
                        wine_name_entry.focus()
                    else:
                        messagebox.showerror(title="Hold up king", message="That wine doesn't appear to be in the "
                                                                           "inventory, double check spelling.")
        except ValueError:
            messagebox.showinfo(title='Wait a second', message='Make sure all the fields are filled out and you are'
                                                               ' entering numerical values for the vintage!')

    home_button = Button(text='Go Back', command=back_to_home)
    home_button.grid(column=0, row=0)
    home_button.config(height=3, width=10)

    search_for_every_wine_button = Button(text='List All Wines', command=search_every_wine)
    search_for_every_wine_button.grid(column=0, row=6)
    search_for_every_wine_button.config(height=3, width=20, pady=5, padx=5)

    search_for_wine_button = Button(text="Search Wines", command=search_wines)
    search_for_wine_button.grid(column=1, row=6)
    search_for_wine_button.config(height=3, width=20, pady=5, padx=5)

    update_count_button = Button(text="Update Count", command=update_counts)
    update_count_button.grid(column=2, row=6)
    update_count_button.config(height=3, width=20, pady=5, padx=5)


def delete_wines_screen():
    window.minsize(width=750, height=425)

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
            wine_name = wine_name_entry.get().title()
            wine_vintage = int(wine_vintage_add.get())
            wine_info = (wine_name, wine_vintage)
            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')
            else:
                with connection:
                    cursor.execute("SELECT * FROM wine WHERE name =:name AND vintage =:vintage", {
                        'name': wine_name, 'vintage': wine_vintage
                    })
                    wine_search = cursor.fetchone()
                    if wine_search is not None:
                        answer = messagebox.askyesno(title='Confirmation', message=f"Are you sure you want to delete "
                                                                                   f"{wine_name}, "
                                                                                   f"Vintage: {wine_vintage}"
                                                                                   f" from the database?")
                        if answer:
                            cursor.execute("DELETE from wine WHERE name = :name AND vintage = :vintage",
                                           { 'name': wine_name, 'vintage': wine_vintage })
                            messagebox.showinfo(title="Completed",
                                                message=f"{wine_name} has been successfully removed.")
                            wine_name_entry.delete(0, END)
                            wine_vintage_add.delete(0, END)
                            wine_name_entry.focus()
                        else:
                            messagebox.showinfo(title='Okay', message='Alrighty then')
                    else:
                        messagebox.showerror(title="Hold up king", message="That wine doesn't appear to be in the "
                                                                           "inventory, double check spelling.")
                wine_name_entry.focus()

        except ValueError:
            messagebox.showerror(title='Vintage', message='Make sure you are filling out both fields and '
                                                          'entering a numerical value for the vintage!')

    addition_button = Button(text="Remove from Inventory", command=remove_from_database)
    addition_button.grid(column=1, row=7)
    addition_button.config(height=3, width=40)

    back_button = Button(text='Back to Home', command=back_to_home)
    back_button.grid(column=0, row=0)


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

window.mainloop()
