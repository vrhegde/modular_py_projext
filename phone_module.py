import Item

class Phone(Item):

  def __init__(self, name, price: float, quantity = 3, broken_phones = 0):
    #call the super function to import all of the attributes from parent class
    super().__init__(
        name, price, quantity
    )
    #Assert that broken phones is greater or equal to 0
    assert broken_phones >= 0, f"broken_phones{broken_phones} is not a valid input"

    self.broken_phones = broken_phones
