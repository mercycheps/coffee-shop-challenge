# coffee-shop-challenge
##  Features

### Models & Properties

- **Customer**
  - Name (1–15 character string)
  - `.orders` → List of Order instances
  - `.coffees` → Unique list of Coffee instances they've ordered
  - `.create_order(coffee, price)` → Creates a new order
  - `most_aficionado(coffee)` (class method) → Customer who spent the most on a given coffee

- **Coffee**
  - Name (at least 3 characters, immutable)
  - `.orders` → List of related Order instances
  - `.customers` → Unique list of Customers who ordered this coffee
  - `.num_orders()` → Total number of orders for this coffee
  - `.average_price()` → Average price of all orders for this coffee

- **Order**
  - Requires a valid `Customer`, `Coffee`, and a `price` (float between 1.0 and 10.0)
  - Read-only `.customer`, `.coffee`, and `.price` properties

###  Relationships
- Many-to-many between `Customer` and `Coffee` via `Order`
- Each `Order` ties a customer and a coffee together with a price

## Usage

1. Clone the repository or copy the files into your local directory.
2. Run the `main.py` script to test the functionality:

```bash
python main.py
