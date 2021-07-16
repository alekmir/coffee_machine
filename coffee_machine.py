class CoffeeMachine:
    def __init__(self):
        self.water_amount = 400
        self.milk_amount = 540
        self.coffee_amount = 120
        self.cups_amount = 9
        self.money_amount = 550
        self.status = "main menu"

    def remaining(self):
        print(f'\nThe coffee machine has:'
              f'\n{self.water_amount} of water'
              f'\n{self.milk_amount} of milk'
              f'\n{self.coffee_amount} of coffee beans'
              f'\n{self.cups_amount} of disposable cups'
              f'\n{self.money_amount} of money\n')

    def cooking(self, water, milk, coffee, cup, price):
        if water > self.water_amount:
            print('Sorry, not enough water!\n')
            return False
        elif milk > self.milk_amount:
            print('Sorry, not enough milk!\n')
            return False
        elif coffee > self.coffee_amount:
            print('Sorry, not enough coffee beans!\n')
            return False
        elif cup > self.cups_amount:
            print('Sorry, not enough cups!\n')
            return False
        else:
            print('I have enough resources, making you a coffee!\n')
            self.water_amount -= water
            self.milk_amount -= milk
            self.coffee_amount -= coffee
            self.cups_amount -= cup
            self.money_amount += price
            return True

    def buy(self):
        self.coffee_to_buy = input('\nWhat do you want to buy? '
                                   '1 - espresso, '
                                   '2 - latte, '
                                   '3 - cappuccino, '
                                   'back - to main menu:\n')
        if self.coffee_to_buy == '1':
            self.buy_espresso()
        elif self.coffee_to_buy == '2':
            self.buy_latte()
        elif self.coffee_to_buy == '3':
            self.buy_cappuccino()
        elif self.coffee_to_buy == 'back':
            return True
        else:
            print("Error! User asking undefined coffee!")

    def buy_espresso(self):
        # Espresso recipe:
        water = 250  # 250 ml of water
        milk = 0  # No milk needed
        coffee = 16  # 16 g of coffee beans
        price = 4  # $4
        cup = 1  # 1 coffee cup

        self.cooking(water, milk, coffee, cup, price)

    def buy_latte(self):
        # Latte recipe:
        water = 350  # 350 ml of water
        milk = 75  # 75 ml of milk
        coffee = 20  # 20 g of coffee beans
        price = 7  # $7
        cup = 1  # 1 coffee cup

        self.cooking(water, milk, coffee, cup, price)

    def buy_cappuccino(self):
        # Cappuccino recipe:
        water = 200  # 200 ml of water
        milk = 100  # 100 ml of milk
        coffee = 12  # 12 g of coffee beans
        price = 6  # $6
        cup = 1  # 1 coffee cup

        self.cooking(water, milk, coffee, cup, price)

    def fill(self):
        self.water_amount += int(input('Write how many ml of water you want to add:\n'))
        self.milk_amount += int(input('Write how many ml of milk you want to add:\n'))
        self.coffee_amount += int(input('Write how many grams of coffee beans you want to add:\n'))
        self.cups_amount += int(input('Write how many disposable coffee cups you want to add:\n'))
        return True

    def take(self):
        print(f'I gave you ${self.money_amount}\n')
        self.money_amount = 0


coffee_machine = CoffeeMachine()
while coffee_machine.status != "off":
    user_choice = input('Write action (buy, fill, take, remaining, exit):\n')
    if user_choice == 'buy':
        coffee_machine.buy()
    elif user_choice == 'fill':
        coffee_machine.fill()
    elif user_choice == 'take':
        coffee_machine.take()
    elif user_choice == 'remaining':
        coffee_machine.remaining()
    elif user_choice == 'exit':
        break
    else:
        print("Error! User asking unknown action")
