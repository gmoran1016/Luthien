import random


def d6():
    return random.randint(1, 6)


class Weapon():
    """The base weapon class"""

    def ___ini___(self, name, description, skillbonus, damage):
        self.name = name
        self.description = description
        self.skillbonus = skillbonus
        self.damage = damage

    def ___str___(self):
        return "{} {} {} {}".format(self.name, self.description, self.skillbonus, self.damage)


class Enemy:
    def ___init___(self, name, health, skill):
        self.name = name
        self.health = health
        self.skill = skill

    def is_alive(self):
        return self.health > 0

    def ___str___(self):
        return "{} {} {}".format(self.name, self.health, self.skill)


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
    print("Skill: {skill} Health: {health} Luck: {luck} Fuel: {fuel}"
          .format(skill=skill, health=health, luck=luck, fuel=fuel))

    print(
        "\nYou find yourself the captain of the Starship Luthien. Congratulations on your promotion!\nAs i'm sure you "
        "are aware you are on the run from the Eridu Empire, The most evil empire in the galaxy")
    print(
        "your goal is simple, navigate the various star systems of the universe and find and destroy the Eridu "
        "Capital ship, simple stuff for a captain such as yourself.\nDuring your journey you will encounter many "
        "things so don't be afraid to fail. Though i'm sure somebody with your skills will be fine. Good luck!")


if __name__ == "__main__":
    main()
