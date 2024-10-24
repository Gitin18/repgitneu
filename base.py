items = {"bread": 1.50, "water": 2.00, "apple": 2.50}

def item_price(item):
    if item in items:
        return items[item]
    else:
        return "The item is not found"

item = "bread"
item = ("apple")

price = item_price(item)
print(f"{item}: {price}")


class Store:
    def __init__(self, name, adress, items=[]):
        self.name = name
        self.adress = adress
        self.items =[]


    def add_apple(self):
        self.items.append('apple')
    def add_water(self):
        self.items.append('water')
    def add_bread(self):
        self.items.append('bread')




    def remove_apple(self):
        self.items.remove('apple')

    def remove_water(self):
        self.items.remove('water')

    def remove_bread(self):
        self.items.remove('bread')

store1 = Store("Name1","Street 1", ['water'])
store2 = Store("Name2","Street 2", ['water'])
store3 = Store("Name3","Street 3", [] )

store1.add_bread()
store1.add_water()
store1.add_apple()
store2.add_apple()
store3.add_bread()
store3.add_bread()

print(f"In Store 1 available", store1.items)
print(f"In Store 2 available",store2.items)
print(f"In Store 3 available",store3.items)





