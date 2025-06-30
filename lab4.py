#TASK 1 - Set Up a Loop Control Variable
checking = 'yes'

while checking == 'Yes' or checking == 'yes':
    print("What is your age?")
    user_input = input()
    if int(user_input) >= 18:
        print("Yes you can vote")
    else:
        print('You cant vote, get lost haha')
    print("Want to input another age?")
    user_input2 = input()
    checking = user_input2


#TASK 2 - Checking Multiple Numbers for Positivity or Negativity
List1 = [3, -1, 0, 6, -4]

for x in List1:
    if x > 0 :
        print(f'{x} is Positive')
    elif x < 0 :
        print(f'{x} is Negative')
    elif x == 0 :
        print(f'{x} has no value')

#TASK 3 - Task 3: Collecting Blocks in Minecraft
inventory = ["TNT", "Glass", "Stone Bricks", "Netherite", "Totem of Undying"]

asking = 'Yes'

while asking == 'Yes' or asking == 'yes':
    print("What item are you looking for?")
    user_input_res = input()
    if user_input_res in inventory:
        print(f'{user_input_res} is in your inventory')
    else:
        print(f'{user_input_res} is not in your inventory')
        
    print("Want to look for another item?")
    user_item_res2 = input()
    asking = user_item_res2

