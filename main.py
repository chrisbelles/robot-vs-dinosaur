from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
from battlefield import Battlefield

robot_one = Robot("R2")
weapon_one = Weapon("axe", 79)

dinosaur_one = Dinosaur("Barney", 90)

battle1 = Battlefield()

battle1.display_welcome()

battle1.battle_phase()