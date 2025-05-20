class Customer:
    
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")
    
    @property
    def orders(self):
        return self._orders
    
    @property
    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee._orders.append(new_order)
        return new_order
    
    @classmethod
    def most_aficionado(cls, coffee):
        spender = None
        max_spent = 0
    
        # Use the customer from each order, not Order.customer
        unique_customers = {order.customer for order in coffee.orders}
    
        for customer in unique_customers:
            total_spent = sum(order.price for order in coffee.orders if order.customer == customer)
            if total_spent > max_spent:
                max_spent = total_spent
                spender = customer
    
        return spender

                

