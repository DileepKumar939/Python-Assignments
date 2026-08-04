# Inventory Management System

inventory = {}

while True:
    print("\n===== INVENTORY MANAGEMENT =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Quantity")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Exit")

    choice = input("Choose Option: ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product] = quantity
        print("Product added successfully.")

    elif choice == "2":
        print("\nAvailable Products")

        for product, qty in inventory.items():
            print(f"{product}: {qty}")

    elif choice == "3":
        product = input("Enter product name: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Quantity updated.")
        else:
            print("Product not found.")

    elif choice == "4":
        product = input("Enter product name: ")

        if product in inventory:
            del inventory[product]
            print("Product deleted.")
        else:
            print("Product not found.")

    elif choice == "5":
        product = input("Enter product name: ")

        if product in inventory:
            print("Quantity:", inventory[product])
        else:
            print("Product not available.")

    elif choice == "6":
        break

    else:
        print("Invalid Choice")