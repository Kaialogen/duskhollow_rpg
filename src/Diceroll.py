import random

class DiceRoll:
    def __init__(self) -> None:
        pass
        
    def rollD20(self) -> int:
        return random.randint(1, 20)
    
    def rollD12(self) -> int:
        return random.randint(1, 12)
    
    def rollD10(self) -> int:
        return random.randint(1, 10)
    
    def rollD8(self) -> int:
        return random.randint(1, 8)
    
    def rollD6(self) -> int:
        return random.randint(1, 6)
    
    def rollD4(self) -> int:
        return random.randint(1, 4)