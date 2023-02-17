#importing Libraries
import random


def hangman():
    # Define the list of words
    word_list = ['python', 'java', 'javascript', 'html', 'css', 'php', 'ruby', 'hello']

    # Select a random word from the list
    word = random.choice(word_list)

    # Create a list to store the correct guesses
    correct_guesses = []

    # Set the number of guesses
    num_guesses = 6
    
    # Loop until the user runs out of guesses or guesses the word
    while num_guesses > 0:
        # Display the current status of the word
        status = ''
        for letter in word:
            if letter in correct_guesses:
                status += letter
            else:
                status += '_'
        print(status)

        # Prompt the user to guess a letter
        guess = input('Guess a letter: ')

        # Check if the guess is correct
        if guess in word:
            correct_guesses.append(guess)
        else:
            num_guesses -= 1
            print('Wrong guess. You have', num_guesses, 'guesses left.')

        # Check if the user has guessed the word
        if set(word) == set(correct_guesses):
            print('Congratulations! You guessed the word.\nThe Word is',word)
            break

    # If the user runs out of guesses, display the game over message
    if num_guesses == 0:
        print('Game over. The word was', word)
    

while True:
    hangman()
    choice = input("Do you want to play again?:\nType \'Y\' for YES and \'N\' for NO: ")
    if choice == "Y" or "y":
        continue
    else:
        print("Thanks for playing\nVisit again!!!")
        break

    



















