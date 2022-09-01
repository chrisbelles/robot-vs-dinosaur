from inspect import _void
from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health =  101
        self.active_weapon = Weapon("axe", 50)


    def attack(self, dinosaur): 
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{dinosaur.name} has taken a devistating strike leaving {dinosaur.health} health.")