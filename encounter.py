class Encounter:
    """The base encounter class"""

    def ___ini___(self, name, description):
        self.name = name
        self.description = description

    def ___str___(self):
        return "{} {}".format(self.name, self.description)