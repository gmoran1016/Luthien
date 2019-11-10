from pip._vendor.distlib.compat import raw_input
import random

import combat

nothing = ['You have a rare moment of solace in this hectic world.', 'The scanners have come up negative, you have a '
                                                                     'moment of peace.', 'Wow there is nothing here, '
                                                                                         'Incredible!',
           'The radar shows '
           'no enemy\'s in '
           'this area.',
           "There are no enemy's here to fight.", "I'm sorry, the enemy you are looking for is in a different castle"]


def store(money, fuel, max_fuel, repairToolAmount, max_health, skill):
    print('Welcome to the store: what can we get for you?')

    print('\n1.) Buy more fuel - Cost 10 Salvage')
    print('\n2.) Buy a repair tool - Cost 10 Salvage')
    print('\n3.) Modify your ship - Cost 50 Salvage')
    print('\n4.) Leave the store')

    while True:
        selection = input('Make a selection (1, 2, 3 or 4): ')
        if money > 9:
            if selection == '1':
                if fuel == max_fuel:
                    print('You already have the max amount of fuel.')

                else:
                    print('Your fuel has been increased by one.')
                    fuel += 1
                    money = money - 10
                    print('Your current fuel is: {}'.format(fuel))

            elif selection == '2':
                repairToolAmount += 1
                money = money - 10
                print("Thank you for your purchase! ")

            elif selection == '3':
                if money >= 50:
                    x = input('Would you like to \n1.) Increase Max Health by 1 \nor \n2.) increase you skill by 1: ')
                    if x == '1':
                        max_health += 1
                        print('your max health is now {}'.format(max_health))
                        money -= 50

                    elif x == '2':
                        skill += 1
                        print('Your skill is now {}'.format(skill))
                        money -= 50

                    else:
                        return money, fuel, max_fuel, repairToolAmount, max_health, skill
                else:
                    print("You don't have enough money")

            elif selection == '4':
                print("Hope to see you again soon!")
                return money, fuel, max_fuel, repairToolAmount, max_health, skill
        else:
            print("Unfortunately you are broke so we can't sell you anything")
            return money, fuel, max_fuel, repairToolAmount, max_health, skill


def station(money, fuel, health, skill):
    while True:
        investigate = input("As you enter this area your radio buzzes to life. 'Please help me Obi Won Kenobi, "
                            "You're my only hope' "
                            "Do you investigate? (y or n)  ")

        if investigate == 'y':
            choice = random.randint(1, 4)
            if choice == 1:
                ##enemy##
                print("Enemy")
                health = combat.enemy(3, skill, health)
                return money, fuel, health, skill

            elif choice == 2:
                ##Salvage##
                print("you find some salvage lying around so you take it")
                salvageamount = random.randint(10, 20)
                money += salvageamount
                print('your current amount of salvage is now: {}'.format(money))
                return money, fuel, health, skill

            elif choice == 3:
                ##Fuel##
                print("You find some fuel canisters lying around so you take them")
                fuelamount = random.randint(0, 10)
                fuel += fuelamount
                print('your current fuel is now: {}'.format(fuel))
                return money, fuel, health, skill

            elif choice == 4:
                # Mines/damage##
                print("You clumsily pilot your ship into an old mine as you investigate")
                healthlost = random.randint(1, 5)
                health -= healthlost
                print('Your current health is now: {}'.format(health))
                return money, fuel, health, skill
            else:
                print('something has gone wrong you should see this!')
                return money, fuel, health, skill

        else:
            return money, fuel, health, skill
