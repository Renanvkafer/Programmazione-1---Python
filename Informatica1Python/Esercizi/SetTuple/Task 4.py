"""
Imagine you run a small grocery store, and you want to manage your inventory efficiently. Create a Python program that allows you to add, update, and check the stock of various products in your store.

1 - Initialize Inventory: Create an empty dictionary named inventory to represent your store's inventory.

2 - Add Products: Add the following products to the inventory dictionary with their respective quantities:
     Product: "Apples", Quantity: 100
     Product: "Bananas", Quantity: 50
     Product: "Milk", Quantity: 20

3 - Update Products: Update the quantity of "Milk" to 30 in the inventory dictionary.

4 - Check Stock: Check the current stock of "Bananas" in the inventory dictionary and print the result.

5 - List All Products: Display the current inventory of your store by iterating through the inventory dictionary.

6 - Remove "Apples" from the inventory dictionary and list all products again to confirm that "Apples" have been removed.

"""


def clear():
    print("\n" * 50)


name_inventory = str(input("enter a inventory name: "))

dictionary = {}

controller_while = 10

while controller_while != 0:
    clear()

    print(f"\nYour Inventory {name_inventory}\n")

    print("List All Products - 1")
    print("Add products - 2")
    print("Update products - 3")
    print("Check Stock - 4")
    print("Remove a product - 5")
    print("Quit system - 0\n")

    controller_while = int(input("enter a option: "))

    if controller_while == 2:
        clear()
        product = str(input("Enter a Product: "))
        quant = int(input("Enter a Quantity: "))
        dictionary[product] = quant
        print(f"Product '{product}' add successfully.")
        input("Press Enter to continue...")

    if controller_while == 5:
        clear()
        remove_product = str(input("Enter a product to remove: "))
        removed = dictionary.pop(remove_product, None)
        if removed is not None:
            print(f"Product '{remove_product}' removed successfully.")
        else:
            print(f"Product '{remove_product}' not found.")
        input("Press Enter to continue...")

    if controller_while == 1:
        clear()
        print(f"{name_inventory}\n")
        print(f"{dictionary}")
        input("Press Enter to continue...")

    if controller_while == 3:
        clear()
        update_product = str(input(f"Choose a item for update: "))

        if update_product in dictionary:
            new_product = str(input("Enter a Product: "))
            new_quant = int(input("Enter a Quantity: "))
            new = {new_product, new_quant}
            removed = dictionary.pop(update_product, None)
            dictionary[new_product] = new_quant
            print(f"Product '{new_product}' updated successfully.")
        else:
            print("Product not found!")

        input("Press Enter to continue...")

    if controller_while == 4:
        clear()
        check_item = str(input(f"Type a item to check in the inventory: "))
        if check_item in dictionary:
            print(f"This item is in Inventory: [{check_item} - {dictionary[check_item]}]")
        else:
            print(f"This item not existing in the Inventory")
        input("Press Enter to continue...")

