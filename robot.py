from inspect import _void


class Robot:

    def __init__(self):
        self.name = ""
        self.health = ()
        self.active_weapon = ()


    def attack(self, dinosaur):
        dinosaur.health -= self.damage