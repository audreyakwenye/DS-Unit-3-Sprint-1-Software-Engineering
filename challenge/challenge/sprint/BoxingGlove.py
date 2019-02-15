from acme import Products

class BoxingGlove(Products):
    """Boxing Glove 
    """
    def __init__(self, name="Product", price=10, weight=10, flammability=0.5, identifier=(random.randint(1000000, 9999999))):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier