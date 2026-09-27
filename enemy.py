import random

class Enemy:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name, health = 50, attackPower = 8):
        self.name = name
        self.health = health
        self.attack_power = attackPower

    def attack(self):
        # Return a random value from 1 through this Hero's attack power.
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        # Subtract damage, but do not allow health to fall below 0.
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
    

    def is_alive(self):
        # Return a Boolean based on this Hero's health.
        return self.health > 0