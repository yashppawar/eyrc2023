# Function to add an item to the inventory list
def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        # Item already exists, update its quantity
        inventory[item_name] += quantity
        print(f"UPDATED Item {item_name}")
    else:
        # Item doesn't exist, add it to the inventory
        inventory[item_name] = quantity
        print(f"ADDED Item {item_name}")

# Function to delete an item from the inventory list
def delete_item(inventory, item_name, quantity):
    if item_name not in inventory:
        # Item doesn't exist in the inventory
        print(f"Item {item_name} does not exist")
    elif inventory[item_name] < quantity:
        # Quantity specified in DELETE operation is greater than available quantity
        print(f"Item {item_name} could not be DELETED")
    else:
        # Update quantity by subtracting the specified amount
        inventory[item_name] -= quantity
        print(f"DELETED Item {item_name}")

# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    N = int(input())  # Number of items in the lab initially
    inventory = {}  # Initialize the inventory dictionary
    
    # Populate the initial inventory
    for _ in range(N):
        item_name, item_quantity = input().split()
        inventory[item_name] = int(item_quantity)
    
    M = int(input())  # Number of operations
    
    # Perform the operations
    for _ in range(M):
        operation, item_name, quantity = input().split()
        quantity = int(quantity)
        
        if operation == "ADD":
            add_item(inventory, item_name, quantity)
        elif operation == "DELETE":
            delete_item(inventory, item_name, quantity)
    
    # Calculate the total quantity of all items in the inventory
    total_quantity = sum(inventory.values())
    
    # Print the total quantity
    print(f"Total Items in Inventory: {total_quantity}")
