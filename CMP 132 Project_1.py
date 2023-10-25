# In this project, you will create an Inventory Management System (IMS) for a retail store using Python 
#   classes. The system will allow the store to keep track of 
#   products, manage stock levels, record sales, and generate reports. 
#   This project is an excellent opportunity to apply object-oriented programming principles to 
#   real-world inventory management.
# Required Functionalities for the IMS
# Product Class
# Create a Product class to represent individual products in the store.
# Each product should have attributes such as name, category, price, quantity in stock, and a unique product identifier.
# Inventory Class
# Implement an Inventory class responsible for managing the store's inventory.
# It should provide methods for adding products, updating stock levels, and retrieving product information.
# Sales and Transactions
# Design a mechanism to record sales transactions.
# Create a Transaction class to represent individual sales, including the products sold, quantities, and total amount.
# Stock Management
# Implement methods to update stock levels when products are purchased or restocked.
# Ensure that the system can handle stock tracking accurately.
# Reports
# Develop functionality to generate various reports, such as current stock levels, sales history, and revenue reports.
# Command-Line Interface (CLI) or Graphic User Interface (GUI) on your choice

class Product:
    def __init__(self,name, category, price, stock_quantity, id):
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
        self.id = id

    def __str__(self):
        return f"Product ID: {self.id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Quantity: {self.stock_quantity}"

class Sale:
    @staticmethod
    def sale(product_id, count):
        for item in Store_Inventory.inventory:
            if item.id == product_id and item.stock_quantity >= count:
                item.stock_quantity -= count
                total_price = item.price * count

                Store_Inventory.money += total_price
                transaction = Transaction(item, count)
                report.add_transaction(transaction)

class Inventory:
    inventory = []
    money = 0

    def add_product(self,name, category, price, stock_quantity, id):
        self.inventory.append(Product(name, category, price, stock_quantity, id))

    def update_stock(self, product_id, count):
        for product in self.inventory:
            if product.id == product_id:
                product.stock_quantity += count
                break

    def get_product_data(self, product_id):
        for product in self.inventory:
            if product.id == product_id:
                print(str(product))
                break

    def print_inventory_items(self):
        for item in self.inventory:
            print(f"    Item id {item.id}: {item.name} for ${item.price} each")

    def checkout(self,product_id):
        for product in self.inventory:
            if product.id == product_id:
                amount_of_items_purchased = 0
                while amount_of_items_purchased == 0:
                    amount_of_items_purchased = (int)(input(f"How many {product.name} would you like to purchase? ({product.stock_quantity} left)   "))
                    if amount_of_items_purchased > product.stock_quantity or amount_of_items_purchased <= 0: 
                        print("Please Enter a valid amount")
                        amount_of_items_purchased = 0
                    else:
                        total = product.price * amount_of_items_purchased
                        print(f"You would like to purchase {amount_of_items_purchased} {product.name} for a total of ${total}")
                        finalize = input("Would you like to finalize your purchase? (Y) / (N)   ")
                        if finalize:
                            print("Thank you for your purchase! Type (R) to see report history later on!")
                            Sale.sale(product.id, amount_of_items_purchased)
Store_Inventory = Inventory()


class Transaction:
    def __init__(self, product, count):
        self.product_name = product.name
        self.count_of_sold = count
        self.sales = product.price * count


class Report:
    transactions = []


    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def print_transactions(self):
        if len(self.transactions) == 0:
            print("No transaction recored")
        else:
            for i, transaction in enumerate(self.transactions):
                print(f"Transaction #{i+1}")
                print(f"    Product: {transaction.product_name}")
                print(f"    Count: {transaction.count_of_sold}")
                print(f"    Sales: ${transaction.sales}")

            print(f"Total Revenue ${Store_Inventory.money}")

report = Report()







Store_Inventory.add_product("Apples", "Fruit", 1, 100, 1)
Store_Inventory.add_product("Bananas", "Fruit", 2, 100, 2)
Store_Inventory.add_product("Skittles", "Candy", 0.5, 100, 3)
Store_Inventory.add_product("Butterfingers", "Candy", 0.75, 100, 4)
Store_Inventory.add_product("Cheerios", "Cereal", 2, 100, 5)
Store_Inventory.add_product("Trix", "Cereal", 3, 100, 6)


# Sale.sale(1, 5)
# Sale.sale(2, 1)
# Sale.sale(3, 2)
# Sale.sale(4, 2)
# Sale.sale(5, 1)




# Store_Inventory.update_stock("app", 25)
# Store_Inventory.get_product_data("app")



running = True
while running:
    action = input("Would you like to purchase a product (P), view product data (D), check report history (H), check balance (B), restock (R), or quit (Q)  ")
    if action == "P" or action == "p":
        print("Items to buy:")
        Store_Inventory.print_inventory_items()
        input_id = (int)(input("Type the ID number of which product you would like to purchase    "))
        if(input_id > 0 and input_id <= 6): 
            Store_Inventory.checkout(input_id)
        else:
            print("Enter a valid ID")
    elif action == "D" or action == "d": 
        Store_Inventory.print_inventory_items()
        input_id = (int)(input("Type the ID number of which product you would like to view    "))
        if(input_id > 0 and input_id <= 6): 
            Store_Inventory.get_product_data(input_id)
        else:
            print("Enter a valid ID")
    elif action == "H" or action == "h":
        report.print_transactions()
    elif action == "B" or action == "b": print(f"Total Balance ${Store_Inventory.money}")
    elif action == "Q" or action == "q": running = False

print("Done Thank you for using")



# report.print_transactions()










