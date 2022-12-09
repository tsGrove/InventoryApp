import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE wine (
                name text,
                grape text,
                glass_price integer
                 )""")


class Wines:
    def __init__(self, name, grape, glass_price):
        self.name = name
        self.grape = grape
        self.glass_price = glass_price


def add_wine(wine):
    with connection:
        cursor.execute("INSERT INTO wine VALUES (:name, :grape, :glass_price)",
                       {"name": wine.name, "grape": wine.grape, "glass_price": wine.glass_price})


def search_wine(wine):
    cursor.execute("SELECT * FROM wine WHERE name=:name", {'name': wine})
    return cursor.fetchall()


def update_price(wine):
    with connection:
        cursor.execute("""UPDATE wine SET glass_price = :glass_price
                    WHERE name =: name""",
                  {'name': wine.name, 'glass_price': wine.glass_price})


def remove_wine(wine):
    with connection:
        cursor.execute("DELETE from wine WHERE name = :name"
                       , {'name': wine.name})


wine_1 = Wines('Shatter', 'Grenache', 13)
wine_2 = Wines('Shatter', 'Syrah', 19)
wine_3 = Wines('Old Ghost', 'Zinfandel', 21)
wine_4 = Wines('Matsu', 'Temp', 18)
wine_5 = Wines('Pinky', 'Rose', 14)

add_wine(wine_1)
add_wine(wine_2)
add_wine(wine_3)
add_wine(wine_4)
add_wine(wine_5)

shit = search_wine("Shatter")
print(shit)

connection.close()

