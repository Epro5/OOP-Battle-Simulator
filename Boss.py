import random
from enemy import enemy

class Boss(enemy):
    def __init__(self, name):
        super().__init__(name, health = 500, attackpower = 30)
        self.gold = 0
    
    def attack(self, hero):
        return random.randint(20, self.attack_power)