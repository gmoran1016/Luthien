import random

import encounter
import combat
from item import *


def d6():
    return random.randint(1, 6)


def main():
    skill = 6 + d6()
    max_health = 12 + d6() + d6()
    health = max_health
    max_fuel = 6 + d6()
    fuel = max_fuel
    money = 50
    system = 1
    repairToolAmount = 1

    print("Welcome to Luthien a text based space adventure game!")
    print("First we will create your character and ship")

    print(
        "Skill: {} Health: {} Fuel: {}".format(skill, health, fuel))

    print(
        "\nYou find yourself the captain of the Starship Luthien. Congratulations on your promotion!\nAs i'm sure you "
        "are aware you are on the run from the Eridu Empire, The most evil empire in the galaxy")
    print(
        "your goal is simple, navigate the various star systems of the universe and find and destroy the Eridu "
        "Capital ship, simple stuff for a captain such as yourself.\nDuring your journey you will encounter many "
        "things so don't be afraid to fail. Though i'm sure somebody with your skills will be fine. Good luck!")
    input("Press enter to continue")
    while system < 5:
        area = 1
        while area < 11:
            print("-------------------------------------------\n"
                  "You are in system {} area {}, You have Skill: {}, Health: {}, Fuel: {}, and Salvage: {}".format
                  (system, area, skill, health, fuel, money))
            rand = random.randint(1, 100)
            if rand < 65:
                health = combat.enemy(system, skill, health)
                rewardMoney = random.randint(1, 5)
                rewardFuel = random.randint(0, 2)
                print("**********************\nYou have gained {} Salvage and {} Fuel".format(rewardMoney, rewardFuel))
                money += rewardMoney
                fuel += rewardFuel
                if fuel > max_fuel:
                    fuel = max_fuel

            elif rand < 75:
                money, fuel, max_fuel, repairToolAmount, max_health, skill = encounter.store(money, fuel, max_fuel,
                                                                                             repairToolAmount,
                                                                                             max_health, skill)

            elif rand < 80:
                money, fuel, health, skill = encounter.station(money, fuel, health, skill)
            else:
                print(encounter.nothing[random.randint(1, len(encounter.nothing))])
            # areaencounter.runLoop()
            if repairToolAmount > 0 and health < max_health:
                selection = input("Would you like to use one of your repair tools (you have {} with a health of {} "
                                  "out of {}), y or n?".format(repairToolAmount, health, max_health))
                if selection == 'y':
                    health += d6() + d6()
                    repairToolAmount -= 1
                    if health > max_health:
                        health = max_health
            input("Press enter to continue")
            if fuel == 0:
                print("Sadly you have run out of and are stranded, you ended the game in system {} area {}".
                      format(system, area))
                exit(0)
            fuel -= 1
            area += 1
        system += 1


if __name__ == "__main__":
    main()
