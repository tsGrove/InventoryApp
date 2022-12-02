from tkinter import *
import tkinter as tk
from screeninfo import get_monitors

app_width = 0
app_height = 0

for m in get_monitors():
    if m.__getattribute__('is_primary'):
        app_width = (m.__getattribute__('width')) * .50
        app_height = (m.__getattribute__('height')) * .50

window = tk.Tk()
window.title('Wine Inventory')
window.minsize(width=int(app_width), height=int(app_height))
window.config(padx=100, pady=50, bg='MAROON')

wine_search = Label(text='Search Wine:')
wine_search.grid(column=0, row=4)
wine_search.config(background='MAROON')
wine_search_entry = Entry(width=50)
wine_search_entry.grid(column=1, row=4)

wine_add = Label(text='Add Wine:')
wine_add.grid(column=0, row=5)
wine_add.config(background='MAROON')
wine_add_entry = Entry(width=50)
wine_search_entry.grid(column=1, row=4)

wine_delete = Label(text='Delete Wine:')
wine_delete.grid(column=0, row=6)
wine_delete.config(background='MAROON')
wine_delete_entry = Entry(width=50)
wine_search_entry.grid(column=1, row=4)


window.mainloop()
