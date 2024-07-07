def display_menu():
    """
    Displays the menu options for the shopping list manager.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add_item(shopping_list):
    """
    Adds an item to the shopping list.

    Parameters:
    shopping_list (list): The current shopping list.
    """
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")


def remove_item(shopping_list):
    """
    Removes an item from the shopping list.

    Parameters:
    shopping_list (list): The current shopping list.
    """
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"Item '{item}' not found in the shopping list.")


def view_list(shopping_list):
    """
    Displays the current shopping list.

    Parameters:
    shopping_list (list): The current shopping list.
    """
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")
    if not shopping_list:
        print("The shopping list is empty.")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()