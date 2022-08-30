from inspect import _void
from robot import Robot

class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 950
        self.attack_power = 83
        
    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} has struck for {self.attack_power}, {robot.name} has {robot.health} remaining.")