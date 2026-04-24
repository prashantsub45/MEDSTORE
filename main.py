from inventory import load_inventory, save_inventory, display_inventory
from sales import sell_medicine
from restock import restock_medicine

FILENAME = "inventory.txt"


def main():
    inventory = load_inventory(FILENAME)

    while True:
        print("\n=== MEDSTORE SYSTEM ===")
        print("1. Display Inventory")
        print("2. Sell Medicine")
        print("3. Restock Medicine")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_inventory(inventory)

        elif choice == "2":
            sell_medicine(inventory)
            save_inventory(FILENAME, inventory)

        elif choice == "3":
            restock_medicine(inventory)
            save_inventory(FILENAME, inventory)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()