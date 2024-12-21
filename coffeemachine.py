MENU = {
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
def coins(drink):
    pennies = int(input("Enter the no of the pennies:"))
    dimes = int(input("Enter the no of the dimes: "))
    nickel = int(input("Enter the no of the nickels: "))
    quarter = int(input("Enter the no of the quarters: "))
    total_value = (pennies*0.01) + (dimes*0.10) + (nickel*0.05) + (quarter*0.25)
    if total_value >= MENU[drink]["cost"]:
     change = total_value - MENU[drink]["cost"]
     print(f"Here's your change: {change}")
     for ingredient, amount in MENU[drink]["ingredients"].items():
            resources[ingredient] -= amount
    else: 
        print("Not enough money")

def check_resources(drink):

    """Check if there are enough resources to make the drink."""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

   



def ask():
    while True:
     x =input("What would you like to drink?(espresso,latte,cappuccino),type report to see resources or 'off' to exit : ").lower()
     if x == "report":
        for key, value in resources.items():
            print(f"{key}: {value}\n", end=' ')
        print()
     elif  x in MENU:
            if check_resources(x):  
                print(f"That would be ${MENU[x]['cost']:.2f}")
                coins(x)
    
     elif x == "off":
        print("Coffee Machine is switched off")
        break
        
     else:
        print("Try again!, wrong input")
ask()
