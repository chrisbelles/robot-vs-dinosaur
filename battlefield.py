from inspect import _void


from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot("R2")
        self.dinosaur = Dinosaur("Barney", 90)


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to the most unlikely battle of your lifetime!")
        print("Tonight we will witness the impossible.")
        print(f"{self.robot.name}, A 4th generation defense-bot will fight for survival against the most primal of predators, {self.dinosaur.name}")

    def battle_phase(self): 
        while self.dinosaur.health > 0 and self.robot.health > 0:
            if self.dinosaur.health >= 0:
                self.dinosaur.attack(self.robot)
                if self.robot.health >= 0:         
                    self.robot.attack(self.dinosaur)

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f"{self.robot.name} is the winner!")
        elif self.robot.health <= 0:
            print(f"{self.dinosaur.name} is the winner!")