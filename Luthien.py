import random


def d6():
    d6var = random.randint(1,6)
    return(d6var)

def main():
    print("Welcome to Luthien a text based space adventure game!")
    print("First we will create your character and ship")
    skill = 6 + d6()
    stamina = 12 + d6() + d6()
    luck = 6 + d6()
    fuel = 6 + d6()
    print("Skill: {skill} Stamina: {stamina} Luck: {luck} Fuel: {fuel}".format(skill=skill, stamina=stamina, luck=luck, fuel=fuel))


if __name__ == "__main__":
    main()
