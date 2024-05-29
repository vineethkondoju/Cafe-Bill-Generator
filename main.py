import mysql.connector
from mysql.connector import Error

# Define coffee and toppings with prices
coffee_menu = {
    'Espresso': 2.50,
    'Americano': 3.00,
    'Latte': 3.50,
    'Cappuccino': 4.00,
    'Mocha': 4.50
}

toppings_menu = {
    'Whipped Cream': 0.50,
    'Caramel Syrup': 0.75,
    'Soy Milk': 0.60,
    'Almond Milk': 0.70,
    'Vanilla Syrup': 0.50,
    'Extra Shot': 1.00
}

def get_customer_info():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    return name, phone

def get_coffee_choice():
    print("Coffee Menu:")
    for coffee, price in coffee_menu.items():
        print(f"{coffee}: ${price:.2f}")
    choice = input("Please choose your coffee: ")
    while choice not in coffee_menu:
        choice = input("Invalid choice. Please choose your coffee: ")
    return choice

def get_toppings():
    print("Toppings Menu:")
    for topping, price in toppings_menu.items():
        print(f"{topping}: ${price:.2f}")
    toppings = []
    while True:
        topping_choice = input("Add a topping (or type 'done' to finish): ")
        if topping_choice.lower() == 'done':
            break
        if topping_choice in toppings_menu:
            toppings.append(topping_choice)
        else:
            print("Invalid topping. Please choose again.")
    return toppings

def calculate_total(coffee_choice, toppings):
    total = coffee_menu[coffee_choice]
    for topping in toppings:
        total += toppings_menu[topping]
    return total

def print_bill(name, phone, coffee_choice, toppings, total):
    print("\n--- BILL ---")
    print(f"Customer: {name}")
    print(f"Phone: {phone}")
    print(f"Coffee: {coffee_choice} - ${coffee_menu[coffee_choice]:.2f}")
    print("Toppings:")
    for topping in toppings:
        print(f"  {topping} - ${toppings_menu[topping]:.2f}")
    print(f"Total: ${total:.2f}")
    print("Thank you for your purchase!")

def save_bill_to_db(name, phone, coffee_choice, toppings, total):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='coffeebilling',
            user='root',
            password='vineeth@123'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            toppings_str = ', '.join(toppings)
            query = """INSERT INTO Bills (customer_name, phone, coffee_choice, toppings, total)
                       VALUES (%s, %s, %s, %s, %s)"""
            data = (name, phone, coffee_choice, toppings_str, total)
            cursor.execute(query, data)
            connection.commit()
            print("Bill saved to database successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    name, phone = get_customer_info()
    coffee_choice = get_coffee_choice()
    toppings = get_toppings()
    total = calculate_total(coffee_choice, toppings)
    print_bill(name, phone, coffee_choice, toppings, total)
    save_bill_to_db(name, phone, coffee_choice, toppings, total)

if __name__ == "__main__":
    main()
