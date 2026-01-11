from Weeapon import iron_sword
from Health_Bar import HealthBar


class Player:
    def __init__(self) -> None:
        self.name = "Kael"
        self.health = 50
        self.max_health = 50
        self.melee_damage = 10
        self.default_weapon = iron_sword
        self.weapon = self.default_weapon
        self.health_bar = HealthBar(self, colour="green")

    def melee_attack(self, target) -> None:
        target.health -= self.weapon.damage + self.melee_damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(
            f"{self.name} dealt {self.weapon.damage + self.melee_damage} damage to {target.name} with {self.weapon.name}"
        )

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a {self.weapon.name}")

    def drop(self) -> None:
        print(f"{self.name} dropped {self.weapon.name}")
        self.weapon = self.default_weapon
