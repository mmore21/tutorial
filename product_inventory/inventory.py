class Inventory:
    def __init__(self):
        self.products = []
    
    def addProduct(self, p):
        self.products.append(p)
    
    def calcValue(self):
        value = 0
        for p in self.products:
            value += p.price
        return value