from math import floor
from Health_Bar import HealthBar
from Weeapon import Bite, Shortsword, Pseudopod


class Monster:
    def __init__(self, name: str, health: int, armour_class: int, dexterity: int, strength: int, weapon) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.armour_class = armour_class
        self.dexterity = dexterity
        self.strength = strength
        self.weapon = weapon
        self.health_bar = HealthBar(self, colour="red")

        self.dexterity_modifier = floor((self.dexterity - 10) / 2)
        self.strength_modifier = floor((self.strength - 10) / 2)

    def __str__(self) -> str:
        return self.name

rat = Monster(name="Rat", health=7, armour_class=12, dexterity=15, strength=7, weapon=Bite)
skeleton = Monster(name="Skeleton", health=13, armour_class=13, dexterity=14, strength=10, weapon=Shortsword)
slime = Monster(name="Gelatinous Cube", health=84, armour_class=6, dexterity=3, strength=14, weapon=Pseudopod)
wolf = Monster(name="Wolf", health=11, armour_class=13, dexterity=15, strength=14, weapon=Bite)