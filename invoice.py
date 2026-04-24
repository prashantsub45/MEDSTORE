import datetime
import uuid


def generate_sales_invoice(cart, total, customer):
    filename = f"sales_{uuid.uuid4().hex}.txt"

    with open(filename, "w") as f:
        f.write("=== SALES INVOICE ===\n")
        f.write(f"Customer: {customer}\n")
        f.write(f"Date: {datetime.datetime.now()}\n\n")

        for item in cart:
            name, brand, unit, qty, discount, cost = item
            f.write(f"{name} ({brand}) | {unit} | Qty: {qty} | Discount: {discount:.2f} | Total: {cost:.2f}\n")

        f.write(f"\nGrand Total: {total:.2f}")

    print(f"Invoice saved as {filename}")


def generate_restock_invoice(cart, total, supplier):
    filename = f"restock_{uuid.uuid4().hex}.txt"

    with open(filename, "w") as f:
        f.write("=== RESTOCK INVOICE ===\n")
        f.write(f"Supplier: {supplier}\n")
        f.write(f"Date: {datetime.datetime.now()}\n\n")

        for item in cart:
            name, brand, unit, qty, cost = item
            f.write(f"{name} ({brand}) | {unit} | Qty: {qty} | Cost: {cost:.2f}\n")

        f.write(f"\nTotal Paid: {total:.2f}")

    print(f"Invoice saved as {filename}")