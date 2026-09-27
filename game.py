from goblin import Goblin
from hero import Hero
from mage import Mage

ARENA_NAME = "The Iron Circle"
def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} won the battle!")
    else:
        print(f"{enemy} won the battle!")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")

    print("")

    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    print("")

    print("The gates are opening...")

    print("")

    goblin = Goblin("Gribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Scribble")

    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    print("")

    hero = Hero("Bob")
    max = Mage("Max")

    battle(hero, goblin)




if __name__ == "__main__":
    main()
