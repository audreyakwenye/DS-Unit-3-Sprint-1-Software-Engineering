from acme import Product

class BoxingGlove(Product):
    """Boxing Glove 
    """
    def __init__(self, name="Product", price=10, weight=10, flammability=0.5, identifier=(random.randint(1000000, 9999999))):
      Product.__init__(self, name="Product", price=10, weight=10, flammability=0.5, identifier=(random.randint(1000000, 9999999)))
    
    def explode(self):
      kaboom = self.flammability * self.weight
      if kaboom >= 0:
        print("...it's a Glove")
    
    def punch(self):
      hitter = self.weight
      if hitter < 5:
            print("That Tickles")
      elif hitter <= 15:
            print("Hey that Hurt!")
      else:
          print("Ouch")
