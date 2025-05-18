class customer:
    
 def __init__(self, name):
  self.name = name
  self._orders = []
  
@property
def name(self):
      return self._name
  
  
@name.setter
  
def name(self, value):
    if isinstance(value, str) and 1<= len(value) <= 15:
          self._name = value
    else:
        raise Exception("Name must be a string between 1 and 15 characters")
  
@property
def orders(self):
      return self._orders

@property
def coffees(self):
      return list({order.coffee for order in self._orders})

@property
def create_order(self,coffee,price):
      from order import Order
      new_order = Order(self,coffee,price)
      self._orders.append(new_order)
      coffee._orders.append(new_order)
      return new_order
      
      
@classmethod
def most_aficiondo(cls, coffee):
      from order import Order
      spender = None
      max_spent = 0
      for customer in {order.customer for order in coffee.orders()}:
            total = sum(order.price for order in coffee.orders() if order.customer == customer)
      if total > max_spent:
       max_spent = total
       spender = customer
       return spender
            
      
