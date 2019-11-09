import random


def d6():
    d6var = random.randint(1,6)
    return(d6var)

def main():
    print("Welcome to Luthien a text based space adventure game!")
    print("First we will create your character and ship")
    max_skill = 6 + d6()
    skill = max_skill
    max_health = 12 + d6() + d6()
    health = max_health
    max_luck = 6 + d6()
    luck = max_luck
    max_fuel = 6 + d6()
    fuel = max_fuel
    money = 50
    print("Skill: {skill} Health: {health} Luck: {luck} Fuel: {fuel}".format(skill=skill, health=health, luck=luck, fuel=fuel))


if __name__ == "__main__":
    main()
