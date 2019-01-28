print("Welcome to the CoinCounter, get ready to enter the amounts of each coin you have!")
pennies = int(input("How many pennies do you have? "))
nickles = int(input("How many nickles do you have? "))
dimes = int(input("How many dines do you have? "))
quarters = int(input("How many quarters do you have? "))
half_dollars = int(input("How many half dollars do you have? "))
dollars = int(input("How many dollar coins do you have? "))
pennies_value = .01
nickles_value = .05
dimes_value = .10
quarters_value = .25
half_dollars_value = .50
dollars_value = 1.00
total = (pennies*pennies_value + nickles*nickles_value + dimes*dimes_value + quarters*quarters_value + half_dollars*half_dollars_value + dollars*dollars_value)
print("You have", pennies, "pennies.")
print("You have", nickles, "nickles.")
print("You have", dimes, "dimes.")
print("You have", quarters, "quarters.")
print("You have", half_dollars, "half dollars.")
print("You have", dollars, "dollar coins.")
print("Congratulations! The value for all of your coins is $", total, "dollars.")