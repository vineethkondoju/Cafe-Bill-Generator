class CoffeeShopBillingMachine:
    def _init_(self):
        self.menu = {
            1: ('Espresso', 2.5),
            2: ('Latte', 3.0),
            3: ('Cappuccino', 3.5),
            4: ('Americano', 2.0),
            5: ('Macchiato', 3.0),
            6: ('Mocha', 4.0),
        }
        self.order = {}

    def display_menu(self):
        print("Menu:")
        for number, (item, price) in self.menu.items():
            print(f"{number}. {item}: ${price}")

    def take_order(self):
        while True:
            try:
                item_number = int(input("Enter the item number (or 0 to finish): "))
                if item_number == 0:
                    break

                if 1 <= item_number <= len(self.menu):
                    quantity = int(input(f"Enter the quantity for {self.menu[item_number][0]}: "))
                    self.order[item_number] = quantity
                else:
                    print("Invalid item number. Please choose from the menu.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def generate_bill(self):
        total_amount = 0.0
        print("\nBilling Details:")
        for item_number, quantity in self.order.items():
            item, price = self.menu[item_number]
            total_item_cost = price * quantity
            print(f"{item} x {quantity}: ${total_item_cost:.2f}")
            total_amount += total_item_cost

        print("\nTotal Amount: ${:.2f}".format(total_amount))

    def generate_token_number(self):
        import random
        return random.randint(1000, 9999)

    def run(self):
        customer_name = input("Enter your name: ")
        print(f"Hello, {customer_name}! Welcome to Hard Rock Cafe")
        self.display_menu()
        self.take_order()
        self.generate_bill()
        token_number = self.generate_token_number()
        print(f"\nThank you, {customer_name}! Your token number is: {token_number}")
        print("Please wait for your order. Enjoy your coffee!")


if __name__ == "_main_":
    billing_machine = CoffeeShopBillingMachine()
    billing_machine.run()