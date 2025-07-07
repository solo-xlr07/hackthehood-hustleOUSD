#LIST OF NAMES
yellow = [
    'Sebastian',
    'Erika',
    'Emari',
    'Jessie',
    'Kwame',
    'Juan',
    'Azhar',
    'Taurean',
    'Vicent',
    "A'moni"
]

#CHECK ROSTER FUNCTIONS (FOR)
def roster(name,yellow):
    for i in range(len(yellow)):
        if(name == yellow[i]):
            return True
    return False

#MAIN FUNCTION
name = 'Erika'
print(f"The student {name} is in the roster: {roster(name, yellow)}")


#WHILE LOOP
def roster_check(name):
    counter = 0
    while(counter < len(yellow)):
        if(name == yellow[counter]):
            return True
        counter += 1

    return False    

name_u = 'n'
print(f"The student {name_u} is in the roster: {roster_check(name_u)}")