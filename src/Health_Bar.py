import os

os.system("")


class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colours: dict = {
        "red": "\033[91m",
        "purple": "\33[95m",
        "blue": "\33[34m",
        "blue2": "\33[36m",
        "blue3": "\33[96m",
        "green": "\033[92m",
        "green2": "\033[32m",
        "brown": "\33[33m",
        "yellow": "\33[93m",
        "grey": "\33[37m",
        "default": "\033[0m",
    }

    def __init__(
        self, entity, length: int = 20, is_coloured: bool = True, colour: str = ""
    ) -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.max_health
        self.current_value = entity.health

        self.is_coloured = is_coloured
        self.colour = self.colours.get(colour) or self.colours["default"]

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(
            f"{self.entity.name}'s HEALTH: {self.entity.health} / {self.entity.max_health}"
        )
        print(
            f"{self.barrier}"
            f"{self.colour if self.is_coloured else ''}"
            f"{remaining_bars * self.symbol_remaining}"
            f"{lost_bars * self.symbol_lost}"
            f"{self.colours['default'] if self.is_coloured else ''}"
            f"{self.barrier}"
        )
