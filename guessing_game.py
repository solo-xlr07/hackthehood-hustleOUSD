# Guessing Game - Antonio, Angel, Nelson

import random 

def generate_random_number(): #Function to generate the number
    choose_number = random.randint(1,100)
    return int(choose_number) #makes sure that number returns as inter

def get_user_guess():
    check = False
    while check == False: 
        print("Guess the number. Its between 1 and 100")
        num_guess = int(input())
        if 1<= num_guess <= 100: #check if user guess is between 1-100
            check = True  #breaks the loop
            return num_guess #returns the number
        else:
            print('Not in range of 1 and 100, try again')

def play_guessing_game():
    secret_number = int(generate_random_number()) #generates number by calling function
    gues_check = False  
    Tries = 0 #measure tries
    while gues_check == False: #starts to loop when false
        guess_of_user = int(get_user_guess()) #allows user to input number for guesses
        if guess_of_user == secret_number: #checks guess
            gues_check = True #when true brekas loop
            Tries += 1 
            print('------------------')
            print(f"That's right, the number was {secret_number}. You did it in {Tries} tries")
            print('------------------')
        elif guess_of_user > secret_number:
            print('------------------')
            print('Number is to high')
            Tries += 1
        else:
            print('------------------')
            print('Number is to low')
            Tries += 1

def review():
    return True #just return true


def game_loop():
    playing = False
    print("Do you want to play the guessing game?(yes/no)")
    anwser_to_play = input()
    print('------------------')
    if anwser_to_play == 'Yes' or anwser_to_play == 'yes': 
        playing = True #starts loop to play
        while playing == True:
            keep_playing = False 
            print('Have fun!!!')
            print('------------------')
            play_guessing_game() #calls function to start playing
            keep_playing = review() #once function above is done,  review is called to break loop
            if keep_playing == True:
                print('Thank you for playing')
                break 

    else:
        print("Okay, Bye")
    
    

#CALLING FUNCTIONS
if __name__ == "__main__": 
    game_loop()

