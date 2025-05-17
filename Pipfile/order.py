class order:
 def __init__(self, customer, coffee, price):
     self._customer = customer
     self._coffee = coffee
     self._price = float(price)
     
     if not isinstance(customer, customer):
         raise TypeError("customer must be a Customer instance")
     
     if not isinstance(coffee, coffee):
         raise TypeError("coffee must be a Coffee instance")
     if not(isinstance(price, float) or isinstance(price, int)) or not (1.0 <= price <= 10.0):
         raise Exception("Price must be a float between 1.0 and 10.0")
     
     
        
