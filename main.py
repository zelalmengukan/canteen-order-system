class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def get_info(self):
        return f"{self.product_name} - {self.price} TL"


# Canteen products and prices (Dictionary)
canteen_products = {
    "toast": 50,
    "tea": 10,
    "fruit juice": 25,
    "water": 5
}

# Creating Product objects
product_objects = {}
for product_name, price in canteen_products.items():
    product_objects[product_name] = Product(product_name, price)

# Menu Loop
while True:
    print("\n--- Canteen Order System ---")
    print("1 - View Products")
    print("2 - Place Order")
    print("3 - Exit")
    
    choice = input("Your choice (1-3): ").strip()

    if choice == "1":
        print("\n--- Canteen Menu ---")
        for product in product_objects.values():
            print(product.get_info())

    elif choice == "2":
        request = input("Enter the name of the product you want to order: ").strip().lower()
        if request in product_objects:
            print("Order received")
            print(product_objects[request].get_info())
        else:
            print("Product not found")

    elif choice == "3":
        print("Program closed")
        break

    else:
        print("Invalid choice, please try again.")
