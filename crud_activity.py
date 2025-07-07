cookbook = []

def create(recipe):
    cookbook.append(recipe)
    print(f"{recipe} has been added to the cookbook")

def read(index):
    if index in range(len(cookbook)):
        print(f'The recipe in index {index} is {cookbook[index]}')
    else:
        print('Sorry bub, list aint long enough or no recipes are there. Go add some')


def update(index,recipe):
    if index < len(cookbook):
        old_recipe = cookbook[index]
        cookbook[index] = recipe
        print(f"Recipe has changed from {old_recipe} to {recipe}; YUMMY!")
    else:
        print(f"There's not that many reciples, there's only, {len(cookbook)} recipes")

def destroy(index):
    if index <len(cookbook):
        remove_recipe = cookbook.pop(index)
        print(f'{remove_recipe} has been removed from the cookbook')
    else:
        print('Input another number')

def list_all_recipes():
    if len(cookbook) == 0:
        print('The cookcook is currently empty, WOMP WOMP. Go find recipes')
    else:
        print("These are the recipes in the cookbook:")
        for i in range(len(cookbook)):
            print(f'{i}: {cookbook[i]}')

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program, Thhank you for using code")
            break
        else:
            print("Invalid choice, please try again.")


main()

# python3 crud_activity.py