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
    
    print("\nYou find yourself the captain of the Starship Luthien. Congratulations on your promotion!\nAs i'm sure you are aware you are on the run from the Eridu Empire, The most evil empire in the galaxy")
    print("your goal is simple, navigate the various star systems of the universe and find and destroy the Eridu Capital ship, simple stuff for a captain such as yourself.\nDuring your journey you will encounter many things so don't be afraid to fail. Though i'm sure somebody with your skills will be fine. Good luck!")


if __name__ == "__main__":
    main()
