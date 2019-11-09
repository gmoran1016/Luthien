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
                money = money- 10
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
                    #Mines/damage##

            else:
                break