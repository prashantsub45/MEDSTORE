from invoice import generate_restock_invoice


def restock_medicine(inventory):
    cart = []
    total = 0

    supplier = input("Enter supplier name: ")

    while True:
        name = input("Medicine name: ")

        if name not in inventory:
            print("Medicine not found.")
            continue

        unit = input("Tablet or Strip: ").lower()
        qty = int(input("Quantity: "))

        med = inventory[name]
        brand = med["brand"]

        if unit == "tablet":
            added = qty
            cost = qty * med["rate_tablet"]

        elif unit == "strip":
            added = qty * med["strip_size"]
            cost = qty * med["rate_strip"]

        else:
            print("Invalid unit.")
            continue

        inventory[name]["stock"] += added
        cart.append((name, brand, unit, qty, cost))
        total += cost

        if input("Add more items? (y/n): ").lower() != 'y':
            break

    generate_restock_invoice(cart, total, supplier)