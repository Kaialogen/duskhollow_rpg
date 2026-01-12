from math import floor
from Health_Bar import HealthBar


class Combatant:
    """
    Base class for any entity that can participate in combat.
    """

    def __init__(
        self,
        name: str,
        health: int,
        armour_class: int,
        dexterity: int,
        strength: int,
        weapon,
        health_bar_colour: str,
    ) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.armour_class = armour_class
        self.dexterity = dexterity
        self.strength = strength
        self.weapon = weapon

        self.dexterity_modifier = floor((dexterity - 10) / 2)
        self.strength_modifier = floor((strength - 10) / 2)

        self.health_bar = HealthBar(self, colour=health_bar_colour)

    def take_damage(self, amount: int) -> None:
        """
        Apply damage and update the health bar.
        """
        self.health = max(self.health - amount, 0)
        self.health_bar.update()

    def roll_attack(self, dice) -> tuple[int, bool]:
        """
        Roll an attack
        
        :param self: Description
        :param dice: Description
        :return: (total_roll, is_critical)
        :rtype: tuple[int, bool]
        """
        d20 = dice.rollD20()
        is_critical = d20 == 20
        total = d20 + self.strength_modifier
        return total, is_critical
    
    def roll_damage(self, dice, critical: bool = False) -> int:
        """
        Roll weapon damage. On a crit, roll damage dice twice.
        
        :param self: Description
        :param dice: Description
        :param critical: Description
        :return: Description
        :rtype: int
        """
        num_dice, sides = self.weapon.damage_dice
        rolls = num_dice * (2 if critical else 1)

        damage = dice.roll(sides, rolls) + self.strength_modifier
        return max(1, damage)

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return self.name
