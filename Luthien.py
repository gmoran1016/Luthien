import random
import time

import encounter
import combat


def d6():
    return random.randint(1, 6)


def main():
    skill = 6 + d6()
    max_health = 12 + d6() + d6()
    health = max_health
    fuel = 6 + d6()
    max_fuel = 20
    money = 50
    system = 1
    repairToolAmount = 1
    print("""\
 __         __  __     ______   __  __     __     ______     __   __    
/\ \       /\ \/\ \   /\__  _\ /\ \_\ \   /\ \   /\  ___\   /\ "-.\ \   
\ \ \____  \ \ \_\ \  \/_/\ \/ \ \  __ \  \ \ \  \ \  __\   \ \ \-.  \  
 \ \_____\  \ \_____\    \ \_\  \ \_\ \_\  \ \_\  \ \_____\  \ \_\\"\_ \ 
  \/_____/   \/_____/     \/_/   \/_/\/_/   \/_/   \/_____/   \/_/ \/_/ 
""")

    print("Welcome to Luthien a text based Space Adventure Game!")
    print("By Brain Zschau & Griffin Moran")
    print(
        "\nYou find yourself the captain of the Starship Luthien. Congratulations on your promotion!\nAs i'm sure you "
        "are aware you are on the run from the Eridu Empire, The most evil empire in the galaxy!")
    print(
        "\nYour goal is simple, navigate the various star systems of the universe and find and destroy the Eridu "
        "Capital ship, simple stuff for a captain such as yourself.\nDuring your journey you will encounter many "
        "things so don't be afraid to fail. Though i'm sure somebody with your skills will be fine. Good luck!")
    input("\nPress enter to continue")
    print("\nFirst we will create your character and ship:")
    print("Skill: {} Health: {} Fuel: {}".format(skill, health, fuel))

    test = input("\nWould you like to Start with 50 extra salvage (1) \nor \n2 Extra repair tools (2): ")
    if test == '1':
        money += 50
        print('You now have {} Salvage'.format(money))
    elif test == '2':
        repairToolAmount += 2
        print('You now have {} Repair Tools'.format(repairToolAmount))
    else:
        print('Fine have it your way')

    input('\nPress enter to continue')
    while system < 5:
        area = 1
        while area < 11:
            print("-------------------------------------------\n"
                  "You are in system {} area {}, You have Skill: {}, Health: {}, Fuel: {}, and Salvage: {}".format(
                system, area, skill, health, fuel, money))
            rand = random.randint(1, 100)
            # Enemy
            if rand < 55:
                health = combat.enemy(system, skill, health)
                rewardMoney = random.randint(1, 5)
                rewardFuel = random.randint(0, 2)
                print("**********************\nYou have gained {} Salvage and {} Fuel".format(rewardMoney, rewardFuel))
                money += rewardMoney
                fuel += rewardFuel
                if fuel > max_fuel:
                    fuel = max_fuel
            # Store
            elif rand < 70:
                money, fuel, max_fuel, repairToolAmount, max_health, skill = encounter.store(money, fuel, max_fuel,
                                                                                             repairToolAmount,
                                                                                             max_health, skill)
            # Station
            elif rand < 75:
                money, fuel, health, skill = encounter.station(money, fuel, max_fuel, health, skill)
                if fuel > max_fuel:
                    fuel = max_fuel
            # Nothing
            else:
                print(encounter.nothing[random.randint(0, len(encounter.nothing) - 1)])
            if repairToolAmount > 0 and health < max_health:
                selection = input(
                    "Would you like to use one of your repair tools (you have {} with a health of {} out of {}), "
                    "y or n?".format(repairToolAmount, health, max_health))
                if selection == 'y':
                    health += d6() + d6()
                    repairToolAmount -= 1
                    if health > max_health:
                        health = max_health
            input("Press enter to continue")
            if fuel == 0:
                selection = input("Sadly you have run out of and are stranded, you ended the game in system {} area {}"
                                  "\n would you like to play again?(y/n)".format(system, area))
                if selection == 'y':
                    main()
                exit(0)
            fuel -= 1
            area += 1
        system += 1

    combat.finalboss(skill, health, max_health, repairToolAmount)
    selection = input(
        "{} has been destroyed!!!!!!!!!!!!!\n CONGRATULATION ON WINNING\nWould you like to play again?(y/n)".format(
            "Eridu"))
    if selection == 'y':
        main()
    exit(0)


if __name__ == "__main__":
    main()
