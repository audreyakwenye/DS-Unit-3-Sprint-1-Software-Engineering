import random 
from acme import Product


product.name = []
product.price = []
product.weight = []
product.flammability = []
product.identifier = []
products = []

class reports:
    """Acme Products List
    """
    def __init__(self, name="Report"):
      self.name = name
    
    def generate_products(self):
      verbs = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
      nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
      for _ in range(30):
          name = (random.choice(verbs) + s + random.choice(nouns))
          product.name.append(name)
          price = random.randint(4,101)
          product.price.append(price)
          weight = random.randint(4,101)
          product.weight.append(weight)
          flammability = random.uniform(0.0, 2.5)
          product.flammability.append(flammability)
          identifier = random.randint(1000000, 9999999)
          product.identifier.append(identifier)
          products.append([name, price, weight, flammability, identifier])
          
    def inventory_report(self):
      unique_names = len(set(product.name))
      average_price = sum(product.price) / len(product.price)
      average_weight = sum(product.weight) / len(product.weight)
      average_flam = sum(product.flammability) / len(product.flammability)
      print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
      print("Unique product names: ", unique_names)
      print("Average price: ", average_price)
      print("Average weight: ", average_weight)
      print("Average flammability: ", average_flam)