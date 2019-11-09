class Item:
    """The base item class"""

    def ___ini___(self, name, description):
        self.name = name
        self.description = description

    def ___str___(self):
        return "{} {}".format(self.name, self.description)


class Weapon:
    """The base weapon class"""

    def ___ini___(self, name, description, skillbonus, damage):
        self.name = name
        self.description = description
        self.skillbonus = skillbonus
        self.damage = damage

    def ___str___(self):
        return "{} {} {} {}".format(self.name, self.description, self.skillbonus, self.damage)