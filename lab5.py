# Lab 5 Nelson Perez-Cordova (Hustle OUSD)

#STEP 1 - Cat Greeting Function
def cat_greeting(word):
    print("Whats the cats name?")
    user_input_name = input()
    print(f"Who is {user_input_name} talking it to?")
    user_input_to = input()
    print(f'{user_input_name} says {word} to {user_input_to}')


#STEP 2 - Superhero Power Function (Fixed Output)
def generate_superhero_power_fixed():
    power = "Ice Beam"
    name = 'Jeff'
    print(f'{name} superpower is {power}')


#STEP 2 - Grow
def grow():
    print('Whats your person name?')
    hero_name = input()
    print('Whats there power?')
    power = input()
    print(f'Does {hero_name} have a enemy?')
    yes_no = input()
    if yes_no == 'yes' or yes_no == 'Yes':
        print(f"What's {hero_name} enemy's name?")
        villian = input()
        print("Where are they fighting?")
        place = input()
        print(f'{hero_name} superpower is {power}. {hero_name} fight {villian} at {place}')
    else:
        print(f'{hero_name} superpower is {power}.')


#STEP 3 - Superhero Power Function with Return
def generate_superhero_power_return():
    print('Whats your favorite superpower?')
    power = input()
    return power


#STEP 4 - Superhero Power Function with Arguments
def generate_superhero_power_arg(name, power):
    message = f"{name} has the power of {power}"
    return message


#STEP 5 - Looping through Greetings 
def cat_greetings_loop():
    for i in range(5):
        print("The cat says meow")


#STEP 5 - Grow
def cat_greeting_grow():
    greetings = []
    print("What's the cat name?")
    cat_name = input()
    print('What will the cat say?')
    greeting = input()
    greetings.append(greeting)
    print('Want to add another greeting for the cat?')
    yes_no = input()
    while yes_no == 'Yes' or yes_no == 'yes':
        print(f'What will {cat_name} say?')
        greet_new = input()
        greetings.append(greet_new)
        print('Want to add another greeting?')
        yes_no = input()
    for i in greetings:
        print(f"{cat_name} says {i}")    
    

#STEP 6 - Superhero Power Function with Multiple Powers
def generate_multiple_powers():
    print('Whats your heroes name?')
    hero = input()
    print(f'What powers does {hero} have?')
    powers = []
    power = input()
    powers.append(power)
    print('Want to add another power?')
    yes_no = input()
    while yes_no == 'Yes' or yes_no == 'yes':
        print(f'What power do you want to add for {hero}?')
        power_new = input()
        powers.append(power_new)
        print('Want to add another power?')
        yes_no = input()
    for i in powers:
        print(f'{hero} has the power of {i}')


#CALLING FUNCTIONS
cat_greeting("Meow") #Step 1
generate_superhero_power_fixed() #Step 2
grow() #Step 2 - Grow
print(generate_superhero_power_return()) #Step 3
print(generate_superhero_power_arg("Kai","Ice Beam")) #Step 4
cat_greetings_loop()#Step 5
cat_greeting_grow()#Step 5 - Grow
generate_multiple_powers()#Step 6
