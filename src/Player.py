from Weeapon import iron_sword
from Combatant import Combatant


class Player(Combatant):
    def __init__(
        self,
        dexterity: int,
        strength: int,
        armour_class: int,
        name: str = "Kael",
        health: int = 50,
    ) -> None:
        super().__init__(
            name=name,
            health=health,
            armour_class=armour_class,
            dexterity=dexterity,
            strength=strength,
            weapon=iron_sword,
            health_bar_colour="green",
        )

        self.default_weapon = iron_sword

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a {weapon.name}")

    def drop(self) -> None:
        print(f"{self.name} dropped {self.weapon.name}")
        self.weapon = self.default_weapon
