class Weapon:
    def __init__(
        self, name: str, weapon_type: str, damage_dice: tuple[int, int], value: int
    ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage_dice = damage_dice
        self.value = value


iron_sword = Weapon(name="Iron Sword", weapon_type="slashing", damage_dice=(1, 8), value=10)

Shortsword = Weapon(name="Shortsword", weapon_type="piercing", damage_dice=(1, 6), value=5)

crossbow = Weapon(name="Crossbow", weapon_type="piercing", damage_dice=(1, 8), value=25)

Pseudopod = Weapon(name="Pseudopod", weapon_type="Acid", damage_dice=(2, 6), value=0)

Bite = Weapon(name="Bite", weapon_type="piercing", damage_dice=(1, 4), value=0)
