 # ---------------------------------------
# SMART VENDING MACHINE
# ---------------------------------------

menu = {
    "M0": ["Chocolate Milk", 2.00, 6, "Drinks"],
    "M1": ["Water", 1.00, 5, "Drinks"],
    "M2": ["7 up", 2.50, 7, "Drinks"],
    "M3": ["Smoothies", 2.00, 9, "Drinks"],
    "M4": ["Milk Tea", 2.00, 8, "Drinks"],
    "I0": ["Chocolate", 2.50, 15, "Snacks"],
    "I1": ["Cup Noodles", 4.20, 9, "Snacks"],
    "I2": ["Chips", 1.30, 8, "Snacks"],
    "I3": ["Ice cream", 2.10, 7, "Snacks"],
    "I4": ["Brownies", 4.00, 6, "Snacks"]
}

def display_menu():
    print("\n--- VENDING MACHINE MENU ---")
    categories = set(item[3] for item in menu.values())
    for category in categories:
        print(f"\n{category}:")
        for code, item in menu.items():
            if item[3] == category:
                print(f"{code} - {item[0]} - £{item[1]:.2f} (Stock: {item[2]})")

def get_product_choice():
    return input("\nEnter item code (or Q to quit): ").upper()

def get_money_input(price):
    total_inserted = 0.0
    while total_inserted < price:
        try:
            money = float(input(f"Insert money (£{price - total_inserted:.2f} remaining): "))
            if money <= 0:
                print("Please insert a positive amount.")
                continue
            total_inserted += money
            if total_inserted < price:
                print(f"Inserted £{total_inserted:.2f}. Still £{price - total_inserted:.2f} to go.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    change = total_inserted - price
    return total_inserted, change

def suggest_item(item_name):
    item_name_lower = item_name.lower()
    if item_name_lower in ["coffee", "milk tea", "smoothies"]:
        print("Suggestion: Would you like to buy a biscuit or snack with your drink?")
    elif item_name_lower in ["coke", "7 up", "water"]:
        print("Suggestion: Chocolate or chips go well with your drink!")
    elif item_name_lower in ["chocolate", "cup noodles", "brownies"]:
        print("Suggestion: Want a drink with that snack?")

def vending_machine():
    print("="*35)
    print("Welcome to the Smart Vending Machine!")
    print("="*35)

    while True:
        display_menu()
        choice = get_product_choice()

        if choice == "Q":
            print("Thank you for using the vending machine! Goodbye!")
            break

        if choice in menu:
            item_name, item_price, stock, category = menu[choice]

            if stock <= 0:
                print(f"Sorry, {item_name} is out of stock.")
                continue

            total_inserted, change = get_money_input(item_price)

            menu[choice][2] -= 1
            print(f"\nDispensing {item_name}...")
            if change > 0:
                print(f"Your change is £{change:.2f}")
            else:
                print("No change.")

            suggest_item(item_name)

            another = input("\nWould you like to buy another item? (Y/N): ").upper()
            if another != "Y":
                print("Thank you for using the Smart Vending Machine! Have a great day!\n")
                break
        else:
            print("Invalid item code. Please try again.")

# Start the program
if __name__ == "__main__":
    vending_machine()
