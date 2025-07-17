from hero import Hero
from ability import Ability
from armor import Armor

def main():
    print("Who's the first hero in this battle?")
    input_hero = input()
    create_hero1 = input_hero
    print("How much health?(MAKE IT FAIR)")
    input_health1 = input()

    print("Who's else is in this battle?")
    input_hero = input()
    create_hero2 = input_hero
    print("How much health?(MAKE IT FAIR)")
    input_health2 = input()

    # Create heroes
    hero1 = Hero(create_hero1, int(input_health1))
    hero2 = Hero(create_hero2, int(input_health2))

# Create some abilities for hero 1
    print(f"LET'S MAKE 3 ABILITIES FOR {create_hero1}!!!")
    count_1st = 0
    hero1_abi = []
    hero1_damage = []
    while count_1st <= 2:
        print("Whats the ability name?")
        ability_made_hero1 = input()
        hero1_abi.append(ability_made_hero1)
        print("How much damage does it do? *Dont be to OP*")
        damage_made_hero1 = int(input())
        if not isinstance(damage_made_hero1, int):
                print("Use number for damage!")
        else:
            hero1_damage.append(damage_made_hero1)
            count_1st += 1

    #shows all abilities
    print(f'Here are {create_hero1} abilities:')
    for i in range(len(hero1_abi)):
        print(f"{i+1}. {hero1_abi[i]} does {hero1_damage[i]} damage") 

# Create some abilities for hero 2
    print(f"LET'S MAKE 3 ABILITIES FOR {create_hero2}!!!")
    count_1st = 0
    hero2_abi = []
    hero2_damage = []
    while count_1st <= 2:
        print("Whats the ability name?")
        ability_made_hero2 = input()
        hero2_abi.append(ability_made_hero2)
        print("How much damage does it do? *Dont be to OP*")

        damage_made_hero2 = int(input())
        if not isinstance(damage_made_hero2, int):
            print("Use number for damage!")
        else:
            hero2_damage.append(damage_made_hero2)
            count_1st += 1
    
    print(f'Here are {create_hero2} abilities:')
    for i in range(len(hero2_abi)):
        print(f"{i+1}. {hero2_abi[i]} does {hero2_damage[i]} damage") 

    #Adding Ability Hero 1
    for i in range(len(hero1_abi)):
        hero1_abi[i] = Ability(hero1_abi[i], hero1_damage[i])
        hero1.add_ability(hero1_abi[i])

    #Adding Ability Hero 2
    for i in range(len(hero2_abi)):
        #print(f"{hero2_abi[i]} does {hero2_damage[i]}")
        hero2_abi[i] = Ability(hero2_abi[i], hero2_damage[i])
        hero2.add_ability(hero1_abi[i])

    # Create some armors
    shield = Armor("Shield", 200)
    armor_plate = Armor("Armor Plate", 200)

    # Add armor to heroes
    hero1.add_armor(shield)
    hero2.add_armor(armor_plate)

    # Print initial stats
    print(f"{hero1.name} Health: {hero1.current_health}")
    print(f"{hero2.name} Health: {hero2.current_health}")

    # Hero1 attacks hero2
    hero1_attack = hero1.sum_attacks()
    print(f"{hero1.name} attacks with a total damage of {hero1_attack}")

    # Hero2 defends
    hero2_defense = hero2.defend()
    print(f"{hero2.name} defends with a total block of {hero2_defense}")

    # Print the final battle result
    final_damage = hero1_attack - hero2_defense
    hero2.current_health -= max(final_damage, 0)
    print(f"{hero2.name}'s Health after attack: {hero2.current_health}")

    # Determine the winner
    if hero2.current_health <= 0:
        print(f"{hero1.name} wins the battle!")
    else:
        print(f"{hero2.name} is still standing!")

    # Battle between two heroes (randomized winner)
    hero1.battle(hero2)

if __name__ == "__main__":
    main()
