import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
# Returns a random interger between 0 and max_damage
        return random.randint(0,self.max_damage)
    

#testing
if __name__ == "__main__":
    fireball = Ability('Fireball',50)
    print(fireball.attack())