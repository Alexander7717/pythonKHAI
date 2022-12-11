print("Write how many cups of coffee you will need:")
cups = int(input(">"))
print("For", cups,"cups of coffee you will need:")
print(cups * 200, "ml of water")
print(cups * 50, "ml of milk")
print(cups * 15, "ml of coffe beans")

need_water = 200
need_milk = 50
need_coffee_beans = 15
water = int(input("Write how many ml of water the coffee machine has:\n>"))
milk = int(input("Write how many ml of milk the coffee machine has:\n>"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n>"))
cups_need = int(input("Write how many cups of coffee will tou need:\n>"))
cup_coffee = min([water // need_water, milk // need_milk, coffee // need_coffee_beans])
if cup_coffee == cups_need:
    print("Yes, I can make that amount of coffee")
elif cup_coffee > cups_need:
    print("Yes, I can make that amount of coffee (and even", cup_coffee - cups_need, "morethan that)")
else:
    print("No, I can make only", cup_coffee, "cups of coffee")

print("Hello user")
print("In a CoffeeMachine = 1000-water , 540-milk , 120-coffee , 9-cups")
class CoffeeMachine:
    water = 1000
    milk = 540
    coffee = 120
    grn = 1100
    cups = 9
    status ="wait"
    counter = 0

    def m_coffee(salf, t_grn, n_water, n_coffee, n_milk = 0):
        if salf.water < n_water:
            print("Sorry, not enough water!")
        elif salf.coffee < n_coffee:
            print("Sorry, not enough coffee!")
        elif salf.milk < n_milk:
            print("Sorry, not enough milk!")
        elif salf.grn < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            salf.water -= n_water
            salf.coffee -= n_coffee
            salf.milk -= n_milk
            salf.cups -= 1
            salf.grn += t_grn

water = 400
milk = 540
cups = 9
coffe_beans = 120
money = 550
print("The coffee machine has: ")
print(water, "ml of water")
print(milk, "ml of milk")
print(coffe_beans, "g of coffee beans")
print(cups, "disposable cups")
print(money, "$ of money")
action = input("Write action (buy, fill, take):\n>")
if action == "buy":
    type_of_coffee = int(input("What do you want to buy? 1-espresso, 2-latte, 3-cappuccino:\n>"))
    if type_of_coffee == 1:
        if water >= 250 and coffe_beans >= 16 and cups >= 1:
            water -= 250
            coffe_beans -= 16
            cups -= 1
            money += 4
        elif type_of_coffee ==  2:
            if water >= 350 and milk >= 75 and cups >= 1 and coffe_beans >= 20 :
                water -= 350
                milk -= 75
                coffe_beans -= 20
                cups -= 1
                money += 7
        elif type_of_coffee == 3:
            if water >= 200 and milk >= 100 and coffe_beans >= 12 and cups >= 1:
                water -= 200
                milk -= 100
                cups -= 1
                money += 6
        elif action == "fill":
            water += int(input("Write how many ml of water you want to add:\n>"))
            milk += int(input("Write how many ml of milk you want to add:\n>"))
            coffe_beans += int(input("Write how many grams of coffee beans you want to add:\n>"))
            cups += int(input("Write how many disposable coffee cups you want to add:\n>"))
        elif action == "take":
            print(f"I gave you {money} ")
            money = 0
print("The coffee machine has: ")
print(water, "ml of water")
print(milk, "ml of milk")
print(coffe_beans, "g of coffee beans")
print(cups, "disposable cups")
print(money, "$ of money")

