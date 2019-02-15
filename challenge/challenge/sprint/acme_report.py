import random 

class reports:
    """Acme Products List
    """
    def __init__(self, name="Report"):
        self.name = name
        self.products = 


    def generate_Products(self):
      verbs = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
      nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
      for _ in range(30):
          products['name'] = (random.choice(verbs) + s + random.choice(nouns))
          products['price'] = random.randint(4,101)
          products['weight'] = random.randint(4,101)
          products['flammability'] = random.uniform(0.0, 2.5)
          products['identifier'] = random.randint(1000000, 9999999)
          print(products)

    def inventory_report(self):
      for name, count in self.reports.unique():
        print('Unique product names', count)