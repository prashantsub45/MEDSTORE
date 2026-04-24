from invoice import generate_sales_invoice


def sell_medicine(inventory):
    cart = []
    total = 0

    customer = input("Enter customer name: ")

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
            if qty > med["stock"]:
                print("Not enough stock.")
                continue

            cost = qty * med["rate_tablet"]
            discount = 0
            inventory[name]["stock"] -= qty

        elif unit == "strip":
            tablets_needed = qty * med["strip_size"]

            if tablets_needed > med["stock"]:
                print("Not enough stock.")
                continue

            cost = qty * med["rate_strip"]
            discount = 0

            if qty >= 2:
                discount = 0.05 * cost
                cost -= discount

            inventory[name]["stock"] -= tablets_needed

        else:
            print("Invalid unit.")
            continue

        cart.append((name, brand, unit, qty, discount, cost))
        total += cost

        if input("Add more items? (y/n): ").lower() != 'y':
            break

    generate_sales_invoice(cart, total, customer)