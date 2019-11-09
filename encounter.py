from pip._vendor.distlib.compat import raw_input
import random

import Luthien


class Encounter:
    """The base encounter class"""

    def ___init___(self, name, description):
        self.name = name
        self.description = description

    def ___str___(self):
        return "{} {}".format(self.name, self.description)

    def runLoop(self):
        return


class Store(Encounter):
    def ___init___(self, name, description):
        super().__init__(name, description)

    def runLoop(self):
        print('Welcome to the store: what can we get for you?')

        print('\n1.) buy more fuel - Cost 10 Salvage')
        print('\n2.) Buy a repair tool - cost 10 Salvage')
        print('\n3.) modify you ship - cost 100')
        print('\n4.) leave the store')
        while True:
            selection = input('make a selection (1, 2, 3 or 4): ')

            if selection == '1':
                if Luthien.fuel == Luthien.max_fuel:
                    print('You already have the max amount of fuel.')

                else:
                    print('your fuel has been increased by one')
                    Luthien.fuel = ++1
                    Luthien.money = --10
                    print('your current fuel is: ' + Luthien.fuel)

            elif selection == '2':
                Luthien.repairToolAmount = ++1
                Luthien.money = --10
                print("Thank you for your purchase!")

            elif selection == '3':
                print("Sorry currently out of stock")

            elif selection == '4':
                print("Hope to see you again soon!")
                print(Luthien.money)
                break


class Station(Encounter):
    def ___init___(self, name, description):
        super().__init__(name, description)

    def runLoop(self):
        while True:
            investigate = raw_input("As you enter this area your radio buzzes to life. 'Please help me Obi Won Kenobi, "
                                    "You're my only hope' "
                                    "Do you investigate? (y or n)  ")

            if investigate == 'y':
                choice = random.randint(1, 4)
                if choice == 1:
                    ##enemy##
                elif choice == 2:
                    ##Salvage##
                elif choice == 3:
                    ##Fuel##
                elif choice == 4:
                    #Mines##

            else:
                break
