import sqlite3
from wines import Wines

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE wine (
                name text,
                grape text,
                glass_price integer
                 )""")
#
# query = input('What wine would you like to search for?\n').lower()


def add_wine(wine):
    with connection:
        cursor.execute("INSERT INTO wine VALUES (:name, :grape, :glass_price)", {"name": wine.name, "grape": wine.grape,
                                                                                 "glass_price": wine.glass_price})


def search_wine(wine):
    cursor.execute("SELECT * FROM wine WHERE name=:name", {'name': wine.name})
    return cursor.fetchall()


def search_grape(wine):
    cursor.execute("SELECT * FROM wine WHERE name=:grape", {'grape': wine.grape})
    return cursor.fetchall()


def update_price(wine):
    with connection:
        cursor.execute("""UPDATE wine SET glass_price = :glass_price
                    WHERE name =: name""",
                  {'name': wine.name, 'glass_price': wine.glass_price})


def remove_emp(wine):
    with connection:
        cursor.execute("DELETE from wine WHERE name = :name", {'name': wine.name})


shatter = Wines('Shatter', 'Grenache', 13)
old_ghost = Wines('Old Ghost', 'Zinfandel', 18)
matsu = Wines('Matsu', 'Tempranillo', 22)
dicks = Wines('Dicks', 'Nasty', 100)
fancy = Wines('Fancy', 'Grenache', 31)

add_wine(shatter)
add_wine(old_ghost)
add_wine(matsu)
add_wine(dicks)
add_wine(fancy)

wines = search_wine(shatter)
results = search_grape(fancy)

print(wines)

connection.close()

