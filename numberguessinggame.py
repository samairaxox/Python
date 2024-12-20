import random

def number_guessing():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number from 1 to 100")
    
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid Input")
        return  


    number_to_guess = random.randint(1, 100)

    
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Enter a guess: "))
        
        if guess > number_to_guess:
            print("Too High")
        elif guess < number_to_guess:
            print("Too Low")
        else:
            print(f"You guessed right! It was {number_to_guess}.")
            return  
        
        attempts -= 1  
        
        if attempts == 0:
            print(f"You have run out of guesses! The number was {number_to_guess}.")
            return  


number_guessing()


    



    

