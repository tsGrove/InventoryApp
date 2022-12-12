class Wines:
    def __init__(self, name, grape, region, glass_price, bottle_price):
        self.name = name
        self.grape = grape
        self.region = region
        self.glass_price = glass_price
        self.bottle_price = bottle_price


name = 'Shea'
name_2 = 'Steven'
name_3 = ''
names = [name, name_2, name_3]
if names == '':
    print("nah")
