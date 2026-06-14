import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():
    res = requests.get(f"{BASE_URL}/inventory")
    print(res.json())


def add_item():
    name = input("Product name: ")

    data = {"product_name": name}

    res = requests.post(f"{BASE_URL}/inventory", json=data)
    print(res.json())


def update_item():
    item_id = input("ID to update: ")
    new_name = input("New product name: ")

    data = {"product_name": new_name}

    res = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=data)
    print(res.json())


def delete_item():
    item_id = input("ID to delete: ")

    res = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    print(res.status_code)


def menu():
    while True:
        print("\n--- Inventory CLI ---")
        print("1. View inventory")
        print("2. Add item")
        print("3. Update item")
        print("4. Delete item")
        print("5. Exit")

        choice = input("> ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            break


if __name__ == "__main__":
    menu()