from inspect import _void


from robot import Robot

class Dinosaur:

    def __init__(self):
        self.name = ""
        self.health = ()
        self.attack_power = ()
        
        def attack(self, robot):
        robot.health -= self.attack_power