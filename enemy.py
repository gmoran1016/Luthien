class Enemy:
    """The base enemy class"""

    def ___init___(self, name, health, skill):
        self.name = name
        self.health = health
        self.skill = skill

    def is_alive(self):
        return self.health > 0

    def ___str___(self):
        return "{} {} {}".format(self.name, self.health, self.skill)