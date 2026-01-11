from Health_Bar import HealthBar


class Monster:
    def __init__(self, name: str, health: int, damage: int, weapon) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.weapon = weapon
        self.health_bar = HealthBar(self, colour="red")

    def attack(self, target) -> None:
        target.health -= self.weapon.damage + self.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(
            f"{self.name} dealt {self.weapon.damage + self.damage} damage to {target.name} with {self.weapon.name}"
        )

    def __str__(self) -> str:
        return self.name
