from collections import defaultdict

class Product:
    """Acme Products 
    """
    def __init__(self, name="Product", price=10, weight=20, flammability=0.5, identifier=(random.randint(1000000, 9999999))):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
        
    def stealability(self):
        """Is the product stealable
        """
        stealability = self.price / self.weight
        if stealability < 0.5:
              print("Not so stelable")
        elif stealability <= 1:
              print("Kinda stelable")
        else:
            print("Very Stealable")
            
    def explode(self):
        """Is the product is flammable 
        """
        kaboom = self.flammability * self.weight
        if kaboom < 10:
              print("...fizzle")
        elif kaboom <= 50:
              print("...boom!")
        else:
            print("BABOOM!!")
