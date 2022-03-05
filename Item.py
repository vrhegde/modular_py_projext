
import csv

class Item:
  # Class level attributes. 
  #Attributes stored here can be overwritten by instance level attributes
  multiplyer = 2 # class level attribute
  list_all = []
  
  
  # Instance constructor. __init__ = instantiate. 'Self' argument is used when defining the class. 
  def __init__(self, name, price: float, quantity = 3):
    
    # Validate that the data is within acceptable parameters
    assert price >= 0, 'Price has to be a positive numerical' 

    #Assign attributes
    self.__name = name
    self.price = price
    self.quantity = quantity

    # This code adds instaces of the class to a list which is stored within the class object.
    Item.list_all.append(self)
    print('I am created')
  
  @property  # property decorator = read only attribute
  def name(self):
     return self.__name

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self): 
    self.price =  self.price * self.multiplyer 
  # string representation of the object. By using __repr__ print(object) prints out a string formatted such that the
  #  string can be copied on to the consol and used to generate the same object. 
  def __repr__(self):
    return(f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})")

  # Method to instantiate multiple objects from a csv
  #This is a class method, so uses the @classmethod decorator

  @classmethod  
  def instantiate_from_csv(cls,file_input):
    with open(file_input, 'r') as f:
      reader_dict = csv.DictReader(f)
      items_list_of_dicts = list(reader_dict)
    for dict_item in items_list_of_dicts:
      Item(
          name = dict_item.get('Name'),
          price = float(dict_item.get('Price')),
          quantity = int(dict_item.get('Quantity')), 
      )

  #static methods don't take 'self' as an argument. They are just regular functions 
  @staticmethod
  def is_integer(input_num):
    # gives a boolean answer on if the input is an integer or not.
    if isinstance(input_num,float):
      return False
    else:
      if isinstance(input_num,int):
        return True  
