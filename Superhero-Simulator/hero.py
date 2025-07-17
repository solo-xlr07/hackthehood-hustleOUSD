# Lab 6 - Nelson Perez
import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        
    def battle(self, opponent):
    # '''Fight another hero and randomly declare a winner'''
        self.opponent = opponent
        print(f"{self.name} battles {opponent.name}! AND...")

        # Randomly choose winner
        winner = random.choice([self.name, opponent.name])
        print(f"{winner} wins the battle!")

    def add_ability(self, ability):
        self.abilities.append(ability)

    def sum_attacks(self): 
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
            
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()

        return total_block


# #TESING
# if __name__ == "__main__":
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)            # Grace Hopper
#     print(my_hero.current_health)  # 200

#     my_hero1 = Hero("Superman", 500)
#     print(my_hero1.name)            
#     print(my_hero1.current_health)  

#     my_hero.battle(my_hero1)
