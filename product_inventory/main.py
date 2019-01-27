from inventory import Inventory
from product import Product

# initialize Inventory instance
inventory = Inventory()

# fill inventory with Product seeds
for i in range(1, 6):
    p = Product(i * 3.0, i, i * 5)
    inventory.addProduct(p)

# output total value to console
print(inventory.calcValue())

# output Product instance info to console
for p in inventory.products:
    print(p.price, p.pId, p.qty)