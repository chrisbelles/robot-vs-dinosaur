from inspect import _void


from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot("R2")
        self.dinosaur = Dinosaur("Barney", 90)
    def run_game(self): _void

    def display_welcome(self):
        startBattle = "n"
        if startBattle == "n":
            print("Welcome to the most unlikely battle of your lifetime!")
            print("Tonight we will witness the impossible.")
            print(f"{self.robot.name}, A 4th generation defense-bot will fight for survival against the most primal of predators, {self.dinosaur.name}")
        startBattle = input("The fighters are ready, are you? y/n: ")

    def battle_phase(self): 
        if self.dinosaur.health > 0 and self.robot.health > 0:
            self.dinosaur.attack()
            self.robot.attack()
        elif self.dinosaur.health <= 0:
            winner = self.robot.name
            print(f"{self.dinosaur.name} has been defeated! Your Champion is {self.robot.name}!!")
        elif self.robot.health <= 0:
            winner = self.dinosaur.name
            print(f"{self.robot.name} has been defeated! Your Champion is {self.dinosaur.name}!!")
        else:
            print(f"{winner} will hold the title for now, Who will be the next challenger?...")



