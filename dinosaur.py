from inspect import _void


class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 950
        self.attack_power = attack_power
        
    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} has struck for {self.attack_power}, {robot.name} has {robot.health} remaining.")