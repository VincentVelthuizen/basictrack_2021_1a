def add_fruit(inventory, fruit, quantity=0):
    if fruit not in inventory:
        inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity


new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print(new_inventory)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory)
