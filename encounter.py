from pip._vendor.distlib.compat import raw_input
import random


def store(money, fuel, max_fuel, repairToolAmount):
    print('Welcome to the store: what can we get for you?')

    print('\n1.) buy more fuel - Cost 10 Salvage')
    print('\n2.) Buy a repair tool - cost 10 Salvage')
    print('\n3.) modify you ship - cost 100')
    print('\n4.) leave the store')
    while True:
        selection = input('make a selection (1, 2, 3 or 4): ')

        if selection == '1':
            if fuel == max_fuel:
                print('You already have the max amount of fuel.')

            else:
                print('your fuel has been increased by one')
                fuel = ++1
                money = money - 10
                print('your current fuel is: ' + fuel)

        elif selection == '2':
            repairToolAmount = ++1
            money = money - 10
            print("Thank you for your purchase!")

        elif selection == '3':
            print("Sorry currently out of stock")

        elif selection == '4':
            print("Hope to see you again soon!")
            print(money)
            return money, fuel, repairToolAmount


def station(money, fuel, health):
    while True:
        investigate = raw_input("As you enter this area your radio buzzes to life. 'Please help me Obi Won Kenobi, "
                                "You're my only hope' "
                                "Do you investigate? (y or n)  ")

        if investigate == 'y':
            choice = random.randint(1, 4)
            if choice == 1:
                ##enemy##
                print('needs to be implemented')
                break
            elif choice == 2:
                ##Salvage##
                salvageamount = random.randint(10, 20)
                money += salvageamount
                break

            elif choice == 3:
                ##Fuel##
                fuelamount = random.randint(0, 10)
                fuel += fuelamount
                break
            elif choice == 4:
                # Mines/damage##
                healthlost = random.random(1, 5)
                health -= healthlost
                break
            else:
                print('something has gone wrong you should see this!')
                break

        else:
            break
