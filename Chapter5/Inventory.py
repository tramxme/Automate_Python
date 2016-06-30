import collections

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    #Sorted the dictionary
    sortedInventory = collections.OrderedDict(sorted(inventory.items()))

    for k, v in sortedInventory.items():
        item_total += v
        print(str(v) + " " + k)
    print("\nTotal number of items: " + str(item_total))



def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)


    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
