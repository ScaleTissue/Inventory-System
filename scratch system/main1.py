credentials = [
    {"username": "Joy", "password": "Culanculan"},
    {"username": "1", "password": "1"},
]

inventory = {
    1: {'CPU': ['Intel i9', 10, 'Ryzen 100', 5]},
    2: {'Motherboards': ['ASUS ROG Strix', 5]},
    3: {'RAM': ['Corsair Vengeance', 20]},
    4: {'ROM': ['sample rom', 5]}, 
    5: {'GPU': ['rtx 4020', 5]}, 
    6: {'PSU': ['psu', 5]}, 
    7: {'Cooling': ['fan', 5]}, 
    8: {'Software': ['windows 15', 5]}
}

log_activities = []

def log_activity(activity):
    log_activities.append(activity)

def view_logs():
    print("Log Activities:")
    for log in log_activities:
        print(log)

# CRUD functions

def create_item():
    print("Select a category number:")
    for number, category in inventory.items():
        print(f"{number}. {list(category.keys())[0]}")  # Print category number and name
    
    category_number = int(input("Enter category number: "))
    if category_number in inventory:
        category_name = list(inventory[category_number].keys())[0]  # Retrieve category name
        item_name = input("Enter item name: ")
        quantity = int(input("Input how many items: "))  # Convert quantity to int
        
        category = inventory[category_number][category_name]  # Access category list
        if item_name in category:
            index = category.index(item_name)
            category[index + 1] += quantity
        else:
            category.extend([item_name, quantity])
        print(f"Item '{item_name}' with quantity {quantity} added to category '{category_name}'.")
        log_activity(f"Added {quantity} of {item_name} to category {category_name}")
    else:
        print(f"Category number '{category_number}' does not exist. Please select a valid category.")

def read_category():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for number, category in inventory.items():
            category_name = list(category.keys())[0]
            item_str = f"\n {number}. {category_name}:"
            for i in range(0, len(category[category_name]), 2):
                item_str += f"\n   - {category[category_name][i]} = {category[category_name][i + 1]}"
            print(item_str)

def update_item():
    print("Select a category number:")
    for number, category in inventory.items():
        print(f"{number}. {list(category.keys())[0]}")  # Print category number and name
    
    category_number = int(input("Enter category number: "))
    if category_number in inventory:
        category_name = list(inventory[category_number].keys())[0]  # Retrieve category name
        old_item_name = input("Enter current item name: ")
        new_item_name = input("Enter new item name: ")
        
        category = inventory[category_number][category_name]  # Access category list
        if old_item_name in category:
            index = category.index(old_item_name)
            category[index] = new_item_name
            print(f"Item '{old_item_name}' updated to '{new_item_name}' in category '{category_name}'.")
            log_activity(f"Updated item '{old_item_name}' to '{new_item_name}' in category '{category_name}'")
        else:
            print(f"Item '{old_item_name}' not found in category '{category_name}'.")
    else:
        print(f"Category number '{category_number}' does not exist.")

def delete_item():
    print("Select a category number:")
    for number, category in inventory.items():
        print(f"{number}. {list(category.keys())[0]}")  # Print category number and name
    
    category_number = int(input("Enter category number: "))
    if category_number in inventory:
        category_name = list(inventory[category_number].keys())[0]  # Retrieve category name
        item_name = input("Enter item name: ")
        
        category = inventory[category_number][category_name]  # Access category list
        if item_name in category:
            index = category.index(item_name)
            current_quantity = category[index + 1]
            quantity_to_delete = int(input(f"Enter quantity to delete (current quantity: {current_quantity}): "))
            
            if quantity_to_delete > current_quantity:
                print(f"Error: Quantity to delete ({quantity_to_delete}) exceeds current quantity ({current_quantity}).")
            else:
                new_quantity = current_quantity - quantity_to_delete
                if new_quantity == 0:
                    category.pop(index)  
                    category.pop(index)  
                    print(f"Item '{item_name}' deleted from category '{category_name}'.")
                    log_activity(f"Deleted item '{item_name}' from category '{category_name}'")
                else:
                    category[index + 1] = new_quantity
                    print(f"Quantity of item '{item_name}' in category '{category_name}' updated to {new_quantity}.")
                    log_activity(f"Updated quantity of item '{item_name}' in category '{category_name}' to {new_quantity}")
        else:
            print(f"Item '{item_name}' not found in category '{category_name}'.")
    else:
        print(f"Category number '{category_number}' does not exist.")

def inventory_menu():
    while True:
        print("\nInventory Management System")
        print("1. Inventory")
        print("2. Add Item")
        print("3. Update Item's Name")
        print("4. Delete Item")
        print("5. View Logs")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            read_category()
        elif choice == '2':
            create_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            view_logs()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def logn():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        matching_credentials = [cred for cred in credentials if cred["username"] == username and cred["password"] == password]
        if matching_credentials:
            print("Welcome User", username)
            log_activity(f"User '{username}' logged in")
            inventory_menu()
            break
        else:
            print("Invalid username or password. Try again.")
            return logn()

def change_pass():
    username = input("Enter your username: ")

    for cred in credentials:
        if cred["username"] == username:
            new_password = input("Enter new password: ")
            cred["password"] = new_password
            print(f"Your new password is: {new_password}")
            log_activity(f"User '{username}' changed their password")
            break
    else:
        print("Username not found.")
        return change_pass()

def before_lg():
    while True:
        print("Inventory System")
        print("\n1. Login")
        print("2. Change Password")
        print("3. View Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            logn()
        elif choice == '2':
            change_pass()
        elif choice == '3':
            read_category()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

before_lg()
