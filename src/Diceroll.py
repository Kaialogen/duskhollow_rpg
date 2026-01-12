import random


class DiceRoll:
    def roll(self, sides: int, times: int = 1) -> int:
        return sum(random.randint(1, sides) for _ in range(times))

    def rollD20(self) -> int:
        return self.roll(20)