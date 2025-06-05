class InventorySystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, quantity):
        if name in self.inventory:
            self.inventory[name] += quantity
            print(f"Updated '{name}' to quantity: {self.inventory[name]}")
        else:
            self.inventory[name] = quantity
            print(f"Added '{name}' with quantity: {quantity}")

    def get_item_quantity(self, name):
        if name in self.inventory:
            print(f"Item: {name}, Quantity: {self.inventory[name]}")
        else:
            print(f"Item '{name}' not found in inventory.")

    def total_quantity(self):
        total = sum(self.inventory.values())
        print(f"Total quantity of all items: {total}")

    def display_menu(self):
        while True:
            print("\n=== Inventory Menu ===")
            print("1. Add or Update Item")
            print("2. Check Item Quantity")
            print("3. Show Total Quantity")
            print("4. Exit")

            choice = input("Select an option (1-4): ")

            if choice == '1':
                name = input("Enter item name: ")
                try:
                    quantity = int(input("Enter quantity: "))
                    self.add_item(name, quantity)
                except ValueError:
                    print("Invalid quantity! Must be an integer.")
            elif choice == '2':
                name = input("Enter item name to look up: ")
                self.get_item_quantity(name)
            elif choice == '3':
                self.total_quantity()
            elif choice == '4':
                print("Exiting Inventory System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the system
if __name__ == "__main__":
    system = InventorySystem()
    system.display_menu()

