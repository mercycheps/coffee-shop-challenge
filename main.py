from order import Order
from customer import Customer
from coffee import Coffee

# Create Customers
alice = Customer("Alice")
bob = Customer("Bob")
charlie = Customer("Charlie")

# Create Coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
mocha = Coffee("Mocha")

# Create Orders
alice.create_order(latte, 3.5)
alice.create_order(mocha, 4.0)
bob.create_order(latte, 4.5)
bob.create_order(latte, 3.0)
charlie.create_order(mocha, 5.0)
charlie.create_order(espresso, 2.5)
charlie.create_order(espresso, 3.5)

# Test most aficionado
print(Customer.most_aficionado(latte).name)     # Should be 'Bob'
print(Customer.most_aficionado(mocha).name)     # Should be 'Charlie'
print(Customer.most_aficionado(espresso).name)  # Should be 'Charlie'

# Test averages
print(latte.average_price())       # → 3.67
print(espresso.average_price())    # → 3.0
print(mocha.average_price())       # → 4.5
