class Product:
    #All product data
    def __init__(self,name, category, price, stock_quantity, id):
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
        self.id = id

    #Returning string format for when printed
    def __str__(self):
        return f"   Product ID: {self.id}\n   Name: {self.name}\n   Category: {self.category}\n   Price: {self.price}\n  Stock Quantity: {self.stock_quantity}"

class Sale:
    @staticmethod
    def sale(product_id, count):
        #Find the product using the ID inside the inventory list
        for item in Store_Inventory.inventory:
            #When the item is found, check if the quantity in stock is greater than the requested amount
            if item.id == product_id and item.stock_quantity >= count:
                #When all requirements met, reduce the stock quantity of product and sell for money
                item.stock_quantity -= count
                total_price = item.price * count

                #Total Revenue increase when sold item
                Store_Inventory.money += total_price

                #Create a transaction to track this sale
                transaction = Transaction("sale",item, count)
                report.add_transaction(transaction)

class Inventory:
    inventory = []
    money = 0

    #Creates a product and adds it to the stores inventory
    def add_product(self,name, category, price, stock_quantity, id):
        self.inventory.append(Product(name, category, price, stock_quantity, id))

    #Called to restock product in inventory
    def update_stock(self, product_id):
        
        #Find the product using the ID inside the inventory list
        for product in self.inventory:
            #When search id is equal to product ID, it will run
            if product.id == product_id:
                #User input for quantity of product to restock
                count = (int)(input(f"How many {product.name} are you going to restock? "))
                #If quantity is 0, then no product will restock and program will reset
                if count == 0:
                    print(f"No {product.name} restocked")
                #If quantity is greater than 0, then increase stock quanitity
                if count > 0:
                    product.stock_quantity += count
                    print(f"Successfully restocked {count} {product.name}")

                    #Create a transaction for restock
                    transaction = Transaction("restock", product, count)
                    report.add_transaction(transaction)
                break

            
    def get_product_data(self, product_id):
        #Find the product using the ID inside the inventory list
        for product in self.inventory:
            if product.id == product_id:
                #When found, returns the string format for the product
                print(str(product))
                break

    #Prints all products in inventory
    def print_inventory_items(self):
        for item in self.inventory:
            print(f"    Item id {item.id}: {item.name} for ${item.price} each")

    #Confirmation for purchase
    #Find the product using the ID inside the inventory list
    def checkout(self,product_id):
        for product in self.inventory:
            if product.id == product_id:
                amount_of_items_purchased = 0
                while amount_of_items_purchased == 0:
                    #User input for quantity of items to purchase
                    amount_of_items_purchased = (int)(input(f"How many {product.name} would you like to purchase? ({product.stock_quantity} left)   "))
                    
                    #If invalid amount to purchase, reset quantity back to 0 and reset
                    if amount_of_items_purchased > product.stock_quantity or amount_of_items_purchased <= 0: 
                        print("Please Enter a valid amount")
                        amount_of_items_purchased = 0
                    else:
                        #Total cost will equal product cost times amount entered
                        total = product.price * amount_of_items_purchased
                        print(f"You would like to purchase {amount_of_items_purchased} {product.name} for a total of ${total}")

                        #If finalized, transaction will occur
                        finalize = input("Would you like to finalize your purchase? (Y) / (N)   ")
                        if finalize == "Y" or finalize == "y":
                            print("Thank you for your purchase! Type (H) to see report history later on!")

                            #Create a sale
                            Sale.sale(product.id, amount_of_items_purchased)
                        else:
                            print("Purchased Cancled!")

#Creates the store inventory class that will hold revenue and products for a store
Store_Inventory = Inventory()


class Transaction:
    #Holds the attributes of a transaction including name, type of transaction, count of items sold, and total price
    def __init__(self, type, product, count):
        self.product_name = product.name
        self.type = type
        self.count_of_sold = count
        self.sales = product.price * count


class Report:
    transactions = []

    #Adds transactions to the history report
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    #Prints all transactions
    def print_transactions(self):
        if len(self.transactions) == 0:
            print("No transaction recored")
        else:
            for i, transaction in enumerate(self.transactions):
                if transaction.type == "sale": print(f"Transaction #{i+1}: (Sale)")
                elif transaction.type == "restock": print(f"Transaction #{i+1}: (Restock)")

                print(f"    Product: {transaction.product_name}")
                print(f"    Count: {transaction.count_of_sold}")
                if transaction.type == "sale": print(f"    Sales: ${transaction.sales}")
            


            print(f"Total Revenue ${Store_Inventory.money}")

report = Report()






#Adding products into the stores inventory
Store_Inventory.add_product("Apples", "Fruit", 1, 100, 1)
Store_Inventory.add_product("Bananas", "Fruit", 2, 100, 2)
Store_Inventory.add_product("Skittles", "Candy", 0.5, 100, 3)
Store_Inventory.add_product("Butterfingers", "Candy", 0.75, 100, 4)
Store_Inventory.add_product("Cheerios", "Cereal", 2, 100, 5)
Store_Inventory.add_product("Trix", "Cereal", 3, 100, 6)




running = True
while running:
    #Start of the program that asks the user what they want to do
    action = input("Would you like to purchase a product (P), view product data (D), check report history (H), check balance (B), restock (R), or quit (Q)  ")
    
    #If user wants to purchase a product
    if action == "P" or action == "p":
        print("Items to buy:")

        #Print all items
        Store_Inventory.print_inventory_items()

        #User input for specic item they want to purchase
        input_id = (int)(input("Type the ID number of which product you would like to purchase    "))

        #ID must be within range of items
        if(input_id > 0 and input_id <= 6): 
            Store_Inventory.checkout(input_id)
        else:
            print("Enter a valid ID")

    #If user wants to check data for product
    elif action == "D" or action == "d": 

        #Print all items
        Store_Inventory.print_inventory_items()

        #User input for specic item they want to view
        input_id = (int)(input("Type the ID number of which product you would like to view    "))

        #ID must be within range of items
        if(input_id > 0 and input_id <= 6): 
            #Prints product data
            Store_Inventory.get_product_data(input_id)
        else:
            print("Enter a valid ID")

    #If user wants to check history report of items purchased or restocked
    elif action == "H" or action == "h":
        #Prints all transactions
        report.print_transactions()

    #If user wants to check total revenue
    elif action == "B" or action == "b": 
        #Prints total revenie
        print(f"Total Balance ${Store_Inventory.money}")

    #If user wants to restock a product
    elif action == "R" or action == "r":
        #Print all items
        Store_Inventory.print_inventory_items()

        #User input for id of item they want to restock
        input_id = (int)(input("Type the ID number of which product you would like to restock    "))

        #ID must be within range of items
        if(input_id > 0 and input_id <= 6): 
            #Restocked product
            Store_Inventory.update_stock(input_id)
        else:
            print("Enter a valid ID")

    #Sets running to false and ends program
    elif action == "Q" or action == "q": running = False


#Final thank you for using application
print("Done Thank you for using")














