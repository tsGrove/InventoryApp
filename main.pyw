import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

FONT = ('Futura', 18, 'normal')
connection = sqlite3.connect('wine_database.db')
cursor = connection.cursor()

try:
    cursor.execute("""CREATE TABLE wine_database (
                    name text,
                    grape text,
                    vintage integer,
                    on_hand integer,
                    bottle_price integer
                     )""")

except sqlite3.OperationalError:
    print('Database exists')


# back_to_home closes the window and reopens the main.pyw program, as a way to reset the window once the user is
# done with the current screen they're on.
def back_to_home():
    window.destroy()
    os.startfile('main.pyw')


# add_wine_screen will destroy the 3 main buttons found on the main screen, adding fields for the user to fill out that
# are required for the user to add new items to the database
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

# add_to_database gathers all the inputs the user provided and will check a few things, first being that all the fields
# are properly filled out, next it checks that the wine entered doesn't already exist inside the database by searching
# for it, and if both those conditionals are met then they are prompted that the addition was successful
    def add_to_database():
        try:
            wine_name = wine_name_entry.get().title()
            wine_grape = wine_grape_entry.get().title()
            wine_vintage = int(wine_vintage_add.get())
            wine_on_hand = int(wine_on_hand_entry.get())
            wine_bottle_price = int(wine_bottle_entry.get())
            wine_info = (wine_name, wine_grape, wine_bottle_price)

            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')

            else:
                with connection:
                    cursor.execute("SELECT * FROM wine_database WHERE name =:name AND vintage =:vintage",
                                   {
                                       'name': wine_name,
                                       'vintage': wine_vintage
                                   })
                    wine = cursor.fetchone()

                    if wine is None:
                        cursor.execute("INSERT INTO wine_database VALUES (:name, :grape, :vintage,"
                                       " :on_hand, :bottle_price)",
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


# search_wines_screen adjusts the window so that 3 new fields are presented, allowing the user to search for an item
# in the database based on the name and varietal parameters, there is also an option to update the current value for
# on_hand and an option for a new window to open that shows every item currently in the database
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

# search_wines takes the user input gathered from the fields in the current screen and does a query through the
# database before presenting the user with information about their query, first making sure the fields are properly
# filled out and then that the wine exists in the database
    def search_wines():
        try:
            wine_name = wine_name_entry.get().title()
            wine_vintage = int(wine_vintage_add.get())
            wine_info = (wine_name, wine_vintage)

            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')

            else:
                with connection:
                    cursor.execute("SELECT * FROM wine_database WHERE name =:name AND vintage =:vintage",
                                   {
                                       'name': wine_name,
                                       'vintage': wine_vintage
                                   })
                    wine = cursor.fetchone()

                    if wine is not None:
                        messagebox.showinfo(title='Info', message=f'Name: {wine[0]}, Varietal: {wine[1]}, '
                                                                  f'Vintage: {wine[2]},\n '
                                                                  f'Bottles on Hand: {wine[3]}, '
                                                                  f'Bottle Price: {wine[4]}')
                        wine_name_entry.focus()

                    else:
                        messagebox.showerror(title='Uh-oh', message="Sorry, looks like that wine"
                                                                    " isn't in the database!")
                        wine_name_entry.focus()

        except ValueError:
            messagebox.showinfo(title='Wait a second', message='Make sure all the fields are filled out and you are'
                                                               ' entering numerical values for the vintage!')

# search_every_wine iterates through each row inside the database and places the information in a now window, and the
# wines are presented as alphabetically descending
    def search_every_wine():
        with connection:
            sqlite_select_query = """SELECT * from wine_database ORDER BY name ASC"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()

            new_window = Toplevel(window)
            new_window.title('All Wines')
            new_window.minsize(600, 600)
            new_window.config(bg='MAROON')

            count = 0

            for row in records:
                name = (row[0])
                grape = (row[1])
                vintage = (row[2])
                on_hand = (row[3])
                bottle_price = (row[4])

                all_wines_label = Label(new_window, text=f"Name: {name}, Grape: {grape}, Vintage: {vintage}, "
                                                         f"On Hand: {on_hand}, Bottle Price: {bottle_price}")
                all_wines_label.config(font=FONT, fg='WHITE', bg='MAROON')
                all_wines_label.grid(column=1, row=count)

                count += 1

        new_home_button = Button(new_window, text='Go Back', command=back_to_home)
        new_home_button.grid(column=1, row=count)
        new_home_button.config(height=3, width=10)

# this is the other button on the search_wines screen that will allow a user to update the current on_hand value of
# the wine the user is searching for
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
                    cursor.execute("SELECT * FROM wine_database WHERE name =:name AND vintage =:vintage",
                                   {
                                       'name': wine_name,
                                       'vintage': wine_vintage
                                   })
                    wine = cursor.fetchone()

                    if wine is not None:
                        cursor.execute("""UPDATE wine_database SET on_hand =:on_hand
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


# delete_wines_screen adjusts the window so that the user is presented 2 fields to fill out, the database is searched
# using parameters provided by the user, and if a match is found the user is prompted with a window asking to confirm
# the removal of the wine from the database, and a confirmation message if it was succesful
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

# remove_from_database takes the input provided by the user, searches through the database for the wine, if it exists
# the user is prompted with a message to double-check that they're okay with removing it, and if so it is done. however
# if the wine does not exist they are prompted with a different message to possibly check spelling, and to make sure
# all fields are properly filled out
    def remove_from_database():
        try:
            wine_name = wine_name_entry.get().title()
            wine_vintage = int(wine_vintage_add.get())
            wine_info = (wine_name, wine_vintage)

            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')

            else:
                with connection:
                    cursor.execute("SELECT * FROM wine_database WHERE name =:name AND vintage =:vintage", {
                        'name': wine_name, 'vintage': wine_vintage
                    })
                    wine_search = cursor.fetchone()
                    if wine_search is not None:
                        answer = messagebox.askyesno(title='Confirmation', message=f"Are you sure you want to delete "
                                                                                   f"{wine_name}, "
                                                                                   f"Vintage: {wine_vintage}"
                                                                                   f" from the database?")
                        if answer:
                            cursor.execute("DELETE from wine_database WHERE name = :name AND vintage = :vintage",
                                           {'name': wine_name, 'vintage': wine_vintage})
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
window.minsize(width=750, height=450)
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
