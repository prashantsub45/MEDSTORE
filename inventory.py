def load_inventory(filename):
    inventory = {}
    with open(filename, "r") as f:
        for line in f:
            name, brand, stock, rt, rs, strip = line.strip().split("|")
            inventory[name] = {
                "brand": brand,
                "stock": int(stock),
                "rate_tablet": int(rt),
                "rate_strip": int(rs),
                "strip_size": int(strip)
            }
    return inventory


def save_inventory(filename, inventory):
    with open(filename, "w") as f:
        for name, data in inventory.items():
            f.write(f"{name}|{data['brand']}|{data['stock']}|{data['rate_tablet']}|{data['rate_strip']}|{data['strip_size']}\n")


def display_inventory(inventory):
    print("\n=== CURRENT STOCK ===")
    for name, data in inventory.items():
        print(f"{name} ({data['brand']}) - Stock: {data['stock']} tablets")