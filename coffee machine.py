menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0
def get_report():
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]
    print(f"Water : {water}ml\nMilk : {milk}ml\nCoffee : {coffee}g\nMoney : ${profit}")
def make_coffee(drink):
    ingre=drink["ingredients"]
    resources["water"]-=ingre["water"]
    resources["milk"]-=ingre["milk"]
    resources["coffee"]-=ingre["coffee"]
def get_coins(drink):
    print("Please insert coins")
    quarters=int(input("How many quarters? "))
    dimes=int(input("How many dimes? "))
    nickels=int(input("How many nickels? "))
    pennies=int(input("How many pennies? "))
    total=(quarters*.25)+(dimes*.10)+(nickels*.05)+(pennies*.01)
    if total<drink["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change=round(total-drink["cost"],2)
        print(f"Here is ${change} in change.\nEnjoy your coffee!!")
        global profit
        profit+=drink["cost"]
        make_coffee(drink)
def check_resources(drink):
    ingredient=drink["ingredients"]
    if ingredient["water"]>resources["water"]:
        print("Sorry there is not enough water.")
    elif ingredient["milk"]>resources["milk"]:
        print("Sorry there is not enough milk.")
    elif ingredient["coffee"]>resources["coffee"]:
        print("Sorry there is not enough coffee")
    else:
        get_coins(drink)

is_on=True
while is_on:
    print("\t\tWelcome to the coffee house!!")
    x=input("What would you like to have?(expresso/latte/cappucino):")
    if x=="off":
        is_on=False
    elif x=="report":
        get_report()
    else:
        drink=menu[x]
        check_resources(drink)

