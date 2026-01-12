from .combatant import Combatant
from .weapon import Bite, Shortsword, Pseudopod


class Monster(Combatant):
    def __init__(
        self,
        name: str,
        health: int,
        armour_class: int,
        dexterity: int,
        strength: int,
        weapon,
    ) -> None:
        super().__init__(
            name=name,
            health=health,
            armour_class=armour_class,
            dexterity=dexterity,
            strength=strength,
            weapon=weapon,
            health_bar_colour="red",
        )


rat = Monster(name="Rat", health=7, armour_class=12, dexterity=15, strength=7, weapon=Bite)
skeleton = Monster(
    name="Skeleton",
    health=13,
    armour_class=13,
    dexterity=14,
    strength=10,
    weapon=Shortsword,
)
slime = Monster(
    name="Gelatinous Cube",
    health=84,
    armour_class=6,
    dexterity=3,
    strength=14,
    weapon=Pseudopod,
)
wolf = Monster(name="Wolf", health=11, armour_class=13, dexterity=15, strength=14, weapon=Bite)
