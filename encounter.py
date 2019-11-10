from pip._vendor.distlib.compat import raw_input
import random


def store(money, fuel, max_fuel, repairToolAmount):
    print('Welcome to the store: what can we get for you?')

    print('\n1.) buy more fuel - Cost 10 Salvage')
    print('\n2.) Buy a repair tool - cost 10 Salvage')
    print('\n3.) leave the store')
    while True:
        selection = input('make a selection (1, 2 or 3): ')
        if money > 0:
            if selection == '1':
                if fuel == max_fuel:
                    print('You already have the max amount of fuel.')

                else:
                    print('your fuel has been increased by one')
                    fuel += 1
                    money = money - 10
                    print('your current fuel is: {}'.format(fuel))

            elif selection == '2':
                repairToolAmount += 1
                money = money - 10
                print("Thank you for your purchase!")

            elif selection == '3':
                print("Hope to see you again soon!")
                print(money)
                return money, fuel, repairToolAmount
        else:
            print("unfortunately you are broke so we can't sell you anything")
            break


def station(money, fuel, health):
    while True:
        investigate = input("As you enter this area your radio buzzes to life. 'Please help me Obi Won Kenobi, "
                            "You're my only hope' "
                            "Do you investigate? (y or n)  ")

        if investigate == 'y':
            choice = random.randint(1, 4)
            if choice == 1:
                ##enemy##
                print('needs to be implemented')
                return money, fuel, health

            elif choice == 2:
                ##Salvage##
                print("you find some salvage lying around so you take it")
                salvageamount = random.randint(10, 20)
                money += salvageamount
                print('your current amount of salvage is now: {}'.format(money))
                return money, fuel, health

            elif choice == 3:
                ##Fuel##
                print("You find some fuel canisters lying around so you take them")
                fuelamount = random.randint(0, 10)
                fuel += fuelamount
                print('your current fuel is now: {}'.format(fuel))
                return money, fuel, health

            elif choice == 4:
                # Mines/damage##
                print("You clumsily pilot your ship into an old mine as you investigate")
                healthlost = random.randint(1, 5)
                health -= healthlost
                print('Your current health is now: {}'.format(health))
                return money, fuel, health
            else:
                print('something has gone wrong you should see this!')
                return money, fuel, health

        else:
            break
