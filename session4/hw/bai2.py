inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ["seashell", "strangeberry", "lint"]
inventory["backpack"].pop(1)
inventory['gold'] = inventory['gold'] + 50
print(inventory)