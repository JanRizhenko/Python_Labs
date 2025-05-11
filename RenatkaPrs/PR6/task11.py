inventory = {
    "key": 3,
    "mace": 1,
    "gold coin": 24,
    "lantern": 1,
    "stone": 10
}

print("Equipment:")
total = 0
for item, count in inventory.items():
    print(f"{count} {item}")
    total += count

print("Total number of things:", total)
