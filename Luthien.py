import random

import encounter
from item import *


def d6():
    return random.randint(1, 6)





def main():
    max_skill = 6 + d6()
    skill = max_skill
    max_health = 12 + d6() + d6()
    health = max_health
    max_luck = 6 + d6()
    luck = max_luck
    max_fuel = 6 + d6()
    fuel = max_fuel
    weapon = LaserMk1
    money = 50
    system = 1
    area = 1
    repairToolAmount = 1

    print("Welcome to Luthien a text based space adventure game!")
    print("First we will create your character and ship")

    print(
        "Skill: {skill} Health: {health} Luck: {luck} Fuel: {fuel}"
            .format(skill=skill, health=health, luck=luck, fuel=fuel))

    print(
        "\nYou find yourself the captain of the Starship Luthien. Congratulations on your promotion!\nAs i'm sure you "
        "are aware you are on the run from the Eridu Empire, The most evil empire in the galaxy")
    print(
        "your goal is simple, navigate the various star systems of the universe and find and destroy the Eridu "
        "Capital ship, simple stuff for a captain such as yourself.\nDuring your journey you will encounter many "
        "things so don't be afraid to fail. Though i'm sure somebody with your skills will be fine. Good luck!")

    while system < 5:
        area = 1
        while area < 11:
            print("-------------------------------------------\n"
                  "You are in system {} area {}, You have {} Skill {} Health {} Luck {} Fuel and {} money".format
                  (system, area, skill, health, luck, fuel, money))
            rand = random.randint(1, 100)
            if rand < 65:
                print("Enemy")
                # areaencounter = encounter.Enemy()
            elif rand < 75:
                print(money)
                print("Store")
                money, fuel, repairToolAmount = encounter.store(money, fuel, max_fuel, repairToolAmount)

            elif rand < 80:
                print("Station")
                # areaencounter = encounter.Station()
            else:
                print("NOTHING")
            #areaencounter.runLoop()
            area += 1
        system += 1


if __name__ == "__main__":
    main()
