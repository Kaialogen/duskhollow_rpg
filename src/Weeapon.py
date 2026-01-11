class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


iron_sword = weapon(name="Iron Sword", weapon_type="Sword", damage=10, value=10)

wooden_club = weapon(name="Wooden Club", weapon_type="Club", damage=5, value=5)

crossbow = weapon(name="Crossbow", weapon_type="Ranged", damage=20, value=20)
