# Items and their prices in the vending machine

items = {
    "1": {"name": "Fanta", "price": 1.50},
    "2": {"name": "Seven up", "price": 2.00},
    "3": {"name": "Water", "price": 1.00},
         "4":{"name":"Sprite","price":1.50},
         "5":{"name":"Coca-cola","price":1.60},
         "6":{"name":"Lays","price":1.00},
         "7":{"name":"Kurkure","price":1.25}, 
         "8":{"name":"Croissant","price":1.52},
         "9":{"name":"Honey bun","price":2.00},
         "10":{"name":"Jalapeno Cheetos","price":1.74},
         "11":{"name":"Fruit roll up","price":0.75},
         "12":{"name":"Kitkat","price":2.00},
         "13":{"name":"Diarymilk","price":1.75},
         "14":{"name":"Flute","price":1.50},
         "15":{"name":"Cookie","price":2.50},
}
#Vending=input("enter the code:")
class VendingMachine:
    def __init__(self):
        self.products = items
        self.balance = 0.0 


    def display_menu(self):
        print("Vending Machine Menu:")
        for code, item in self.products.items(): 
            print(f"{code}: {item['name']} - ${item['price']:.2f}")



    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted: ${amount}, Total Balance: ${self.balance:.2f}")

    def select_product(self, code):
        if code in self.products:
            product = self.products[code]
            if self.balance >= product['price']:
                self.balance -= product['price']
                print(f"Dispensing {product['name']}. Remaining Balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print("Invalid product code. Please select a valid product.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0.0

# Main execution
vending_machine = VendingMachine()

while True:
    vending_machine.display_menu()

    try:
        amount = float(input("Insert money (q to exit): $"))
        if amount == 0:
            break
        vending_machine.insert_money(amount)

        product_code = input("Enter the code of the product you want to buy: ")
        vending_machine.select_product(product_code)

    except ValueError:
        print("Invalid input. Please enter a valid amount.")

    # Ask if the consumer wants to buy anything else
    purchase_more = input("Are you willing to buy anything else? (yes/no): ")
    if purchase_more.lower() == 'no':
        vending_machine.return_change() 
        break
 
print("Thank you for purchasing from the vending machine ,enjoy")

   



            











