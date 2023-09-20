# Decorator

def upgrade_to_meal(func):
    def inner(amount, taxes, meal_plan):
        if meal_plan == 1:
            print("upgrading the medium meal..")
            print("+add coke")
            print("+add fries")
            amount += 200
            taxes = 0.20

        elif meal_plan == 2:
            print("upgrading to large meal..")
            print("+added large coke")
            print("+added large fries")
            print("+added ice cream")
            amount += 200
            taxes = 0.20
        else:
            print("Thank You for your purchase..")
        return func(amount, taxes, meal_plan)

    return inner

@upgrade_to_meal
def buy_burger(amount , taxes, meal_plann=0):
    return amount + (amount*taxes)

amount_to_pay=buy_burger(amount = 100, taxes = 0.10, meal_plan = 1)

print("Mc Donald's final Price: " , amount_to_pay)
